var express = require('express');
var bodyParser = require('body-parser')

class Todo {
  constructor(task, isFinished = false) {
    this.task = task
    this.is_finished = isFinished
  }
}


var app = express()
var todos = []


app.use(bodyParser.json())

app.get('/todo', (_, resp) => {
  resp.send(JSON.stringify(todos))
})

app.post('/todo', (req, resp) => {
  todo = new Todo(req.body.task)
  todos.push(todo)
  resp.send(JSON.stringify(todo))
})

app.get('/todo/:id', (req, resp) => {
  resp.send(JSON.stringify(todos[req.params.id]))
})

app.post('/todo/:id', (req, resp) => {
  todos[req.params.id].is_finished = req.body.is_finished
  resp.send(JSON.stringify(todos[req.params.id]))
})

app.listen(8000, function () {
  console.log('Running on port 8000!')
});