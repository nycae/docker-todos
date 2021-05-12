#!/usr/bin/python3

from fastapi import FastAPI, HTTPException
from json import JSONEncoder
from pydantic import BaseModel


class Todo(BaseModel):
    task: str = ""
    is_finished: bool = False


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


app = FastAPI()
todo_manager = TodoManager()
todo_serializer = TodoSerializer()


def abort_if(condition, with_status=400):
    if condition:
        raise HTTPException(status_code=with_status)


@app.get("/todo")
def get_todos():
    todos = todo_manager.get_all_todos()
    return todo_serializer.encode(todos)


@app.post("/todo")
def new_todo(todo: Todo):
    todos = todo_manager.post_todo(todo)
    return todo_serializer.encode(todos)


@app.get("/todo/{id}")
def get_todo(id: int):
    todo = todo_manager.get_single_todo(id)
    return todo_serializer.encode(todo)


@app.post("/todo/{id}")
def update_todo(id: int, todo: Todo):
    updated_todo = todo_manager.get_single_todo(id)
    updated_todo.is_finished = todo.is_finished
    todo_manager.update_todo(id, updated_todo)
    return todo_serializer.encode(updated_todo)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
