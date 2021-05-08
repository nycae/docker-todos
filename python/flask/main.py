#!/usr/bin/python3

from flask import Flask, jsonify, request, abort
from json import JSONEncoder


class Todo:
    def __init__(self, task, is_finished = False):
        self.task = task
        self.is_finished = is_finished


class TodoSerializer(JSONEncoder):
    def default(self, o):
        return o.__dict__


class TodoManager:
    def __init__(self):
        self.todos = []

    def get_all_todos(self):
        return self.todos

    def post_todo(self, todo):
        self.todos.append(todo)
        return self.todos[-1]

    def get_single_todo(self, index):
        return self.todos[index]

    def update_todo(self, index, todo):
        self.todos[index] = todo
        return self.todos[index]
    

app = Flask(__name__)
todo_manager = TodoManager()
todo_serializer = TodoSerializer()

def abort_if(condition, with_status=400):
    if condition:
        abort(with_status)

@app.route("/todo", methods=["GET", "POST"])
def manage_todos():
    if request.method=="GET":
        todos=todo_manager.get_all_todos()
    if request.method=="POST":
        abort_if(not request.json or not "task" in request.json, with_status=400)
        todos=todo_manager.post_todo(Todo(request.json["task"]))
    return todo_serializer.encode(todos)

@app.route("/todo/<int:id>", methods=["GET", "POST"])
def manage_todo(id):
    todo=todo_manager.get_single_todo(id)
    if request.method=="POST":
        abort_if(not request.json or not "is_finished" in request.json, with_status=400)
        todo.is_finished = request.json["is_finished"]
        todo_manager.update_todo(id, todo)
    return todo_serializer.encode(todo)

if __name__=='__main__':
    app.run(port=8000)