package com.nycae.todoapp.services;

import java.util.ArrayList;
import com.nycae.todoapp.models.Todo;

import org.springframework.stereotype.Service;

// Yeah, yeah, I know, this should be an interface, blablabla, fuck java and OOP, tbh.
@Service
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
