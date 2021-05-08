#!/usr/bin/python3

import requests


todos = ["Finish this api", "Build the dockers"]


if __name__=='__main__':
    for todo in todos:
        print(requests.post("http://localhost:8000/todo", json={"task": todo}).text)
    print(requests.get("http://localhost:8000/todo").text)
    print(requests.post("http://localhost:8000/todo/0", json={"is_finished": True}).text)
    print(requests.get("http://localhost:8000/todo/0").text)