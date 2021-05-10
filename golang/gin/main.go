package main

import (
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

type todo struct {
	Task       string `json:"task"`
	IsFinished bool   `json:"is_finished"`
}

var todos []todo

func GetTodos(c *gin.Context) {
	c.JSON(http.StatusOK, todos)
}

func NewTodo(c *gin.Context) {
	var todo todo

	if err := c.BindJSON(&todo); err != nil {
		c.AbortWithStatus(http.StatusBadRequest)
		return
	}

	todos = append(todos, todo)
	c.JSON(http.StatusOK, todo)
}

func GetTodo(c *gin.Context) {
	index, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		c.AbortWithStatus(http.StatusBadRequest)
		return
	}
	c.JSON(http.StatusOK, todos[index])
}

func UpdateTodo(c *gin.Context) {
	var todo todo
	index, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		c.AbortWithStatus(http.StatusBadRequest)
		return
	}

	if err := c.BindJSON(&todo); err != nil {
		c.AbortWithStatus(http.StatusBadRequest)
		return
	}

	todos[index].IsFinished = todo.IsFinished
	c.JSON(http.StatusOK, todos[index])
}

func main() {
	gin.SetMode(gin.ReleaseMode)
	r := gin.Default()

	r.GET("/todo", GetTodos)
	r.POST("/todo", NewTodo)
	r.GET("/todo/:id", GetTodo)
	r.POST("/todo/:id", UpdateTodo)

	http.ListenAndServe(":8000", r)
}
