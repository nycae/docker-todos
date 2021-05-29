const Koa = require('koa')
const Router = require('koa-router')
const BodyParser = require('koa-body-parser')

class Todo {
  constructor(task, isFinished = false) {
    this.task = task
    this.is_finished = isFinished
  }
}

const app = new Koa()
const todoManager = new Router()

app.use(BodyParser())

var todos = []

todoManager
  .get('/todo', (ctx) => {ctx.body = todos})
  .get('/todo/:id', (ctx) => {ctx.body = todos[ctx.params.id]})
  .post('/todo', (ctx) => {
    newTodo = new Todo(ctx.request.body.task)
    todos.push(newTodo)
    ctx.body = newTodo
  })
  .post('/todo/:id', (ctx) => {
    todos[ctx.params.id].is_finished = ctx.request.body.is_finished
    ctx.body = todos[ctx.params.id]
  })

app.use(todoManager.routes()).use(todoManager.allowedMethods())
app.listen(8000)