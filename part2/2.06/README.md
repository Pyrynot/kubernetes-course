# Commands used:


Switching namespace:
```console
$ kubens exercise-namespace
✔ Active namespace is "exercise-namespace"
```

Building and pushing:
```console
docker compose build
docker compose push
```

Applying:
```console
$ kubectl apply -f manifests/
configmap/pingponglog-configmap created
deployment.apps/pingponglog-dep created
ingress.networking.k8s.io/pingponglog-ingress created
service/pingponglog-svc created
```

Curling addresses:
```console
$ curl http://localhost:8081
{"file content":"this text is from file","env variable":"hello world","log":"2024-08-04T19:24:55.980241: 7ad350e01c33d3455bcee38bd32f6ee1837e2486e159f8fb006a6c37ede9e273. Ping / Pongs: 1"}(.venv) 

$ curl http://localhost:8081/pingpong
"pong 2"(.venv) 

$ curl http://localhost:8081
{"file content":"this text is from file","env variable":"hello world","log":"2024-08-04T19:25:11.044679: 2c509ba7087707140439630c37ffd9929da016b8c1bc2184c21b4841678c9468. Ping / Pongs: 2"}(.venv)
```