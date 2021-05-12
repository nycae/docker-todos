package com.nycae.todoapp.models;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Todo {
    @JsonProperty("task") 
    private String task;
    @JsonProperty("is_finished") 
    private Boolean isFinished = false;

    public Todo(String task, Boolean isFinished) {
        this.task = task;
        // Seriously, who would develop in a language where binary variables
        // can have 3 values? Fuck you, true false and null.
        this.isFinished = isFinished == null ? false : isFinished; 
    }

    public String getTask() {
        return this.task;
    }

    // Should be named isFinished(), but the fucking serializer breaks.
    public Boolean getIsFinished() {
        return this.isFinished;
    }

    public void setFinished(Boolean isFinished) {
        this.isFinished = isFinished;
    }
}
