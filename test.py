#!/usr/bin/python3

import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument('-s', "--sails", dest="is_sails", help="Use -s or --sails if you are testing sails", action="store_true")

args = parser.parse_args()
todos = ["Finish this api", "Build the dockers"]



if __name__=='__main__':
    for todo in todos:
        print(requests.post("http://localhost:8000/todo", json={"task": todo}).text)
    print(requests.get("http://localhost:8000/todo").text)

    if args.is_sails:
        print(requests.patch("http://localhost:8000/todo/1", json={"is_finished": True}).text)
        print(requests.get("http://localhost:8000/todo/1").text)
    else:
        print(requests.post("http://localhost:8000/todo/0", json={"is_finished": True}).text)
        print(requests.get("http://localhost:8000/todo/0").text)