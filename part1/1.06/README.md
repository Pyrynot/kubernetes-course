# Commands used:


Creating service:
```console
$ kubectl apply -f manifests/service.yaml 
service/todo-app-svc created
```

curling the address:
```console
$ curl http://localhost:8082
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