package com.nycae.todoapp.services;

import javax.inject.Singleton;
import java.util.ArrayList;

import com.nycae.todoapp.models.Todo;

@Singleton
public class TodoService {
    private ArrayList<Todo> todos;

    public TodoService() {
        this.todos = new ArrayList<Todo>();
    }

    public ArrayList<Todo> getTodos() {
        return todos;
    }

    public Todo newTodo(Todo todo) {
        todos.add(todo);
        return todo;
    }

    public Todo getTodo(int id) {
        return todos.get(id);
    }

    public Todo updateTodo(int id, Todo todo) {
        Todo updatedTodo = todos.get(id);
        updatedTodo.setFinished(todo.getIsFinished());
        return updatedTodo;
    }
}
