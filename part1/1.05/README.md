# Commands used:

Building:
```console
docker build -t todo-app:1.05 -t pyrynot/todo-app:1.05 .
```

Re-pushing with correct tag:
```console
docker push pyrynot/todo-app:1.05
```


Updating configs:
```console
$ kubectl apply -f manifests/deployment.yaml 
deployment.apps/todo-app configured
```

Looking at logs to make sure it works and uses the port defined in the deployment.yaml:
```console
$ kubectl logs todo-app-6fb46cc895-mgsth
INFO:     Started server process [1]
INFO:     Waiting for application startup.
Server started on port 8010
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8010 (Press CTRL+C to quit)
```

Starting port-forwarding:
```console
$ kubectl port-forward todo-app-6fb46cc895-mgsth 8010:8010
Forwarding from 127.0.0.1:8010 -> 8010
Forwarding from [::1]:8010 -> 8010
Handling connection for 8010
```

curling the address:
```console
$ curl http://localhost:8010
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>Welcome to my to-do app!</p>
</body>
</html>
```