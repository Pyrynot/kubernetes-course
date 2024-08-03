# Commands used:

Building:
```console
$ docker build -t pyrynot/log-output:1.07 -t log-output:1.07 .
```

Re-pushing with correct tag:
```console
$ docker push pyrynot/log-output:1.07
```


Updating configs:
```console
$ kubectl apply -f manifests/
deployment.apps/log-output unchanged
ingress.networking.k8s.io/dwk-material-ingress unchanged
service/log-output-svc configured
```


curling the address:
```console
$ curl http://localhost:8081/status
{"timestamp":"2024-08-03T19:13:19.332480","random_string":"19193573-4831-4fac-9e4d-12615535a20d"}(.venv) 
```