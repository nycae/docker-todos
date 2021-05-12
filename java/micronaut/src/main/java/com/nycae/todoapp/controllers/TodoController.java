package com.nycae.todoapp.controllers;

import javax.inject.Inject;
import java.util.ArrayList;

import com.nycae.todoapp.services.TodoService;
import com.nycae.todoapp.models.Todo;

import io.micronaut.context.annotation.Parameter;
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Post;

@Controller("/todo")
public class TodoController {
    
    private final TodoService todoService;

    @Inject
    public TodoController(TodoService todoService) {
        this.todoService = todoService;
    }

    @Get(produces = MediaType.TEXT_JSON)
    public ArrayList<Todo> getTodos() {
        return this.todoService.getTodos();
    }

    @Post(produces = MediaType.TEXT_JSON)
    public Todo postTodo(@Body Todo todo) {
        return this.todoService.newTodo(todo);
    }

    @Get(value="/{id}", produces = MediaType.TEXT_JSON)
    public Todo getTodo(@Parameter int id) {
        return this.todoService.getTodo(id);
    }

    @Post(value="/{id}", produces = MediaType.TEXT_JSON)
    public Todo updateTodo(@Parameter int id, @Body Todo todo) {
        return this.todoService.updateTodo(id, todo);
    }
}
