# Commands used:

Building:
```console
$ docker build -t pyrynot/pingpong-app:1.09 -t pingpong-app:1.09 .
```

Re-pushing with correct tag:
```console
$ docker push pyrynot/pingpong-app:1.09 
```


Updating configs:
```console
$ kubectl apply -f manifests/
deployment.apps/pingpong-app-dep created
ingress.networking.k8s.io/combined-ingress created
service/pingpong-app-svc created
```


checking deps:
```console
$ kubectl get deployments.apps
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
todo-app-dep       1/1     1            1           93m
log-output         1/1     1            1           45m
pingpong-app-dep   1/1     1            1           61s
```

checking ingresses:
```console
$ kubectl get ingress
NAME               CLASS    HOSTS   ADDRESS                            PORTS   AGE
todo-app-ingress   <none>   *       172.31.0.3,172.31.0.4,172.31.0.5   80      23m
combined-ingress   <none>   *       172.31.0.3,172.31.0.4,172.31.0.5   80      84s
```

curling both apps:
```console
$ curl localhost:8081/status
{"timestamp":"2024-08-03T19:46:49.373649","random_string":"19193573-4831-4fac-9e4d-12615535a20d"}(.venv)      

$ curl localhost:8081/pingpong
"pong 22"(.venv)
```