# Commands used:


Building, pushing:
```console
$ docker compose build && docker compose push
```

Curling:
```console
$ curl http://localhost:8081/todos
[{"content":"SKrrtt"},{"content":"sdfsdf"},{"content":"Test 123"},{"content":"Read https://en.wikipedia.org/wiki/Heinrich_Parler"},{"content":"Read https://en.wikipedia.org/wiki/Victoria,_Honduras"},{"content":"Read https://en.wikipedia.org/wiki/Meetle_Mice"}](.venv) 
```

Checking the backend container logs to make sure the endpoint is called from the cronjob:
```console
$ kubectl logs todo-app-dep-7c5cf8dcc9-frl28 -c todo-backend
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     10.42.1.4:44230 - "GET /todos HTTP/1.1" 200 OK
INFO:     10.42.1.4:39206 - "GET /todos HTTP/1.1" 200 OK
INFO:     10.42.1.4:34722 - "GET /todos HTTP/1.1" 200 OK
INFO:     10.42.1.4:34722 - "GET /todos HTTP/1.1" 200 OK
INFO:     10.42.1.29:53982 - "POST /todos/random HTTP/1.1" 200 OK
INFO:     10.42.1.4:51036 - "GET /todos HTTP/1.1" 200 OK
INFO:     10.42.1.4:48426 - "GET /todos HTTP/1.1" 200 OK
INFO:     10.42.0.12:57892 - "POST /todos/random HTTP/1.1" 200 OK
INFO:     10.42.1.4:48426 - "GET /todos HTTP/1.1" 200 OK
INFO:     10.42.1.4:48426 - "GET /todos HTTP/1.1" 200 OK
INFO:     10.42.1.4:49654 - "GET /todos HTTP/1.1" 200 OK
INFO:     10.42.0.13:33528 - "POST /todos/random HTTP/1.1" 200 OK
INFO:     10.42.1.4:53528 - "GET /todos HTTP/1.1" 200 OK
```