#!/bin/sh

API_ENDPOINT=${API_ENDPOINT:-"http://todo-backend-svc:8000/todos/random"}

curl -X POST $API_ENDPOINT