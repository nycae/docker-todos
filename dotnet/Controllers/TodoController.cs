using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

using dotnet.Models;

namespace dotnet.Controllers
{
    [ApiController]
    [Route("/todo")]
    public class TodoController : ControllerBase
    {
        private static List<Todo> Todos = new List<Todo>();

        public TodoController()
        {

        }

        [HttpGet]
        public IEnumerable<Todo> GetTodos()
        {
            return Todos;
        }

        [HttpGet("{id}")]
        public Todo GetTodo(int id)
        {
            return Todos[id];
        }

        [HttpPost]
        public Todo NewTodo([FromBody] Todo todo)
        {
            Todos.Add(todo);
            return todo;
        }

        [HttpPost("{id}")]
        public Todo UpdateTodo(int id, [FromBody] Todo todo)
        {
            var updatedTodo = Todos[id];
            updatedTodo.isFinished = todo.isFinished;

            return updatedTodo;
        }
    }
}
