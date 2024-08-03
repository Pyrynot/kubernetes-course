# Commands used:

Retagging:
```console
docker tag todo-app:latest pyrynot/todo-app:1.04
```

Re-pushing with correct tag:
```console
docker push pyrynot/todo-app:1.04
```

Creating a deployment with the yaml:
```console
$ kubectl apply -f manifests/deployment.yaml
deployment.apps/todo-app created
```

Checking deps:
```console
$ kubectl get deployments.apps
NAME       READY   UP-TO-DATE   AVAILABLE   AGE
todo-app   1/1     1            1           12s
```

Looking at logs to make sure it works:
```console
$ kubectl logs -f todo-app-594cbd6bb7-wxrqj 
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
Server started on port 8000
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```