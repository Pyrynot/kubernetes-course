# Commands used:


Apply:
```console
$ kubectl apply -f manifests/
configmap/pingponglog-configmap unchanged
deployment.apps/pingponglog-dep configured
service/postgres-svc unchanged
secret/postgres-secret unchanged
service/pingponglog-svc unchanged
statefulset.apps/postgres-ss configured
(.venv)
```

Checking for IPs:
```console
$ kubectl get svc
NAME              TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                                        AGE
pingponglog-svc   LoadBalancer   34.118.239.191   34.147.205.84   8000:31070/TCP,8001:30966/TCP,8020:32744/TCP   18m
postgres-svc      ClusterIP      None             <none>          5432/TCP                 
                      18m
(.venv) 
```

Curling the ping pong app:
```console
$ curl http://34.147.205.84:8020/pingpong
"pong 1"(.venv)

$ curl http://34.147.205.84:8020/pingpong
"pong 2"(.venv) 

$ curl http://34.147.205.84:8020/pingpong
"pong 3"(.venv) 
```