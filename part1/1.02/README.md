# Commands used:

Building the image:
```console
docker build -t todo-app:latest .
```

Making sure it works:
```console
docker run -d -p 8000:8000 todo-app:latest
```

Checking docker logs:
```console
$ docker logs happy_bell
INFO:     Started server process [1]
INFO:     Waiting for application startup.
Server started on port 8000
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     172.17.0.1:47004 - "GET / HTTP/1.1" 200 OK
```

Tagging the image:
```console
docker tag todo-app:latest pyrynot/todo-app:latest
```

Pushing the image:
```console
docker push pyrynot/todo-app:latest
```

Creating a deployment:
```console
kubectl create deployment todo-app --image=pyrynot/todo-app
```

Checking deployments:
```console
$ kubectl get deployments.apps 
NAME       READY   UP-TO-DATE   AVAILABLE   AGE
todo-app   1/1     1            1           13s
```

Checking that it works:
```console
$ kubectl logs -f todo-app-55cdb9c596-wzfdk 
INFO:     Started server process [1]
INFO:     Waiting for application startup.
Server started on port 8000
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```