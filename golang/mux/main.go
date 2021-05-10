package main

import (
	"encoding/json"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
)

type todo struct {
	Task       string `json:"task"`
	IsFinished bool   `json:"is_finished"`
}

var todos []todo

func GetTodos(w http.ResponseWriter, _ *http.Request) {
	json.NewEncoder(w).Encode(todos)
}

func NewTodo(w http.ResponseWriter, r *http.Request) {
	var todo todo

	if err := json.NewDecoder(r.Body).Decode(&todo); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	todos = append(todos, todo)
	json.NewEncoder(w).Encode(todo)
}

func GetTodo(w http.ResponseWriter, r *http.Request) {
	index, err := strconv.Atoi(mux.Vars(r)["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	json.NewEncoder(w).Encode(todos[index])
}

func UpdateTodo(w http.ResponseWriter, r *http.Request) {
	var todo todo
	index, err := strconv.Atoi(mux.Vars(r)["id"])

	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	if err := json.NewDecoder(r.Body).Decode(&todo); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	todos[index].IsFinished = todo.IsFinished
	json.NewEncoder(w).Encode(todos[index])
}

func main() {
	r := mux.NewRouter()

	r.HandleFunc("/todo", GetTodos).Methods("GET")
	r.HandleFunc("/todo", NewTodo).Methods("POST")
	r.HandleFunc("/todo/{id}", GetTodo).Methods("GET")
	r.HandleFunc("/todo/{id}", UpdateTodo).Methods("POST")

	http.ListenAndServe(":8000", r)
}
