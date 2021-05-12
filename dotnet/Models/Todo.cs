using System;
using System.Text.Json.Serialization;
using Microsoft.AspNetCore.Mvc;

namespace dotnet.Models
{
    [Serializable]
    public class Todo
    {
        [JsonPropertyName("task")] public String task { get; set; }
        [JsonPropertyName("is_finished")]  public Boolean isFinished { get; set; }

        public Todo(String task = "", Boolean isFinished = false)
        {
            this.task = task;
            this.isFinished = isFinished;
        }
    }
}