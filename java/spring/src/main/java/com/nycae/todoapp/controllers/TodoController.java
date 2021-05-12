package com.nycae.todoapp.controllers;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.ArrayList;
import com.nycae.todoapp.models.Todo;
import com.nycae.todoapp.services.TodoService;

@RestController
@RequestMapping("/todo")
public class TodoController {
    private TodoService todoService;

    @Autowired
    public TodoController(TodoService todoService) {
        this.todoService = todoService;
    }
    
    @GetMapping
    public ArrayList<Todo> getTodos() {
        return this.todoService.getTodos();
    }

    @PostMapping
    public Todo createTodo(@RequestBody Todo todo) {
        return this.todoService.newTodo(todo);
    }

    @GetMapping(path = "/{id}")
    public Todo getTodo(@PathVariable int id) {
        return this.todoService.getTodo(id);
    }

    @PostMapping(path = "/{id}")
    public Todo updateTodo(@PathVariable int id, @RequestBody Todo todo) {
        return this.todoService.updateTodo(id, todo);
    }
}
