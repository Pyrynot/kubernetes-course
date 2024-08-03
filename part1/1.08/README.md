# Commands used:


deleting old ingress:
```console
$ kubectl delete ingress dwk-material-ingress 
ingress.networking.k8s.io "dwk-material-ingress" deleted
```

changing configs:
```console
$ kubectl apply -f manifests/
deployment.apps/todo-app-dep unchanged
ingress.networking.k8s.io/todo-app-ingress created
service/todo-app-svc configured
```

checking ingress:
```console
$ kubectl get ingress
NAME               CLASS    HOSTS   ADDRESS                            PORTS   AGE
todo-app-ingress   <none>   *       172.31.0.3,172.31.0.4,172.31.0.5   80      58s
```

curling app address:
```console
$ curl http://localhost:8081
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