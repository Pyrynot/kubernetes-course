#!/bin/sh

API_ENDPOINT=${API_ENDPOINT:-"http://todo-app-svc:8000/todos/random"}

curl -X POST $API_ENDPOINT