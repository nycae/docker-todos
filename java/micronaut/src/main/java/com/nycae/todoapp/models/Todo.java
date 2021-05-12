package com.nycae.todoapp.models;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.micronaut.context.annotation.Property;

public class Todo {
    @Property(name = "task")
    private String task;

    @JsonProperty("is_finished")
    @Property(name = "is_finished", defaultValue = "false")
    private Boolean isFinished = false;

    public Todo() {
        this.task = "";
        this.isFinished = false;
    }

    public Todo(String task, Boolean isFinished) {
        this.task = task;
        // Seriously, who would develop in a language where binary variables
        // can have 3 values? Fuck you, true false and null.
        this.isFinished = isFinished == null ? false : isFinished; 
    }

    public String getTask() {
        return this.task;
    }
    public void setTask(String task) {
        this.task = task;
    }

    // Should be named isFinished(), but the fucking serializer breaks.
    public Boolean getIsFinished() {
        return this.isFinished;
    }

    public void setFinished(Boolean isFinished) {
        this.isFinished = isFinished;
    }
}
