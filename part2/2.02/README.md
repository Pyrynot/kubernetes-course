# Current project:


Building and pushing:
```console
docker compose build
docker compose push
```


Applying:
```console
$ kubectl apply -f manifests/
deployment.apps/todo-app-dep created
ingress.networking.k8s.io/todo-app-ingress created
persistentvolume/image-cache-pv unchanged
persistentvolumeclaim/image-cache-pvc unchanged
service/todo-app-svc created
```


Checking logs after creating two to-do's:
```console
$ kubectl logs todo-app-dep-59bcb86cbf-md67q -c todo-backend
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     10.42.1.4:33684 - "GET /todos HTTP/1.1" 200 OK
INFO:     10.42.1.4:33690 - "POST /todos HTTP/1.1" 200 OK
INFO:     10.42.1.4:33690 - "GET /todos HTTP/1.1" 200 OK
INFO:     10.42.1.4:33690 - "POST /todos HTTP/1.1" 200 OK
INFO:     10.42.1.4:55530 - "GET /todos HTTP/1.1" 200 OK
INFO:     10.42.1.4:55530 - "GET /todos HTTP/1.1" 200 OK
```


Curling the address:
```console
$ curl http://localhost:8081/todos
[{"content":"Testi"},{"content":"Mitä"}](.venv)

$ curl -X POST "http://localhost:8081/todos" -H "Content-Type: application/json" -d '{"content": "My new todo"}'
{"content":"My new todo"}(.venv)

$ curl http://localhost:8081/todos
[{"content":"Testi"},{"content":"Mitä"},{"content":"My new todo"}](.venv)
```