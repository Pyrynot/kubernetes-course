# Commands used:


Apply:
```console
$ kubectl apply -f manifests/
configmap/pingponglog-configmap unchanged
deployment.apps/pingponglog-dep unchanged
ingress.networking.k8s.io/pingponglog-ingress configured
service/postgres-svc unchanged
secret/postgres-secret unchanged
service/pingponglog-svc unchanged
statefulset.apps/postgres-ss configured
```

Checking for ingress:
```console
$ kubectl get ing
NAME                  CLASS    HOSTS   ADDRESS        PORTS   AGE
pingponglog-ingress   <none>   *       34.36.81.252   80      20m
```

Curling the ping pong app:
```console
$ curl http://34.36.81.252/
{"file content":"this text is from file","env variable":"hello world","log":"2024-08-07T20:29:30.707024: 1ff2806444bcfc1f1535acb7279e262718d873dd2dd5eb82876fe502771f7c72. Ping / Pongs: 7"}(.venv) 

$ curl http://34.36.81.252/pingpong
"pong 8"(.venv) 

$ curl http://34.36.81.252/
{"file content":"this text is from file","env variable":"hello world","log":"2024-08-07T20:29:40.796742: 27f8d4862a9bc8d9cfd2e80d004b584494743b19f196c2d55edc6076ab11ed5d. Ping / Pongs: 8"}(.venv) 
```

Listing resources:
```console
$ kubectl get all
NAME                                   READY   STATUS    RESTARTS   AGE
pod/pingponglog-dep-84f895d7d5-xnpl8   3/3     Running   0          4m51s
pod/postgres-ss-0                      1/1     Running   0          72m

NAME                      TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                                        AGE
service/pingponglog-svc   NodePort    34.118.239.191   <none>        8000:31070/TCP,8001:30966/TCP,8020:32744/TCP   72m
service/postgres-svc      ClusterIP   None             <none>        5432/TCP                                       72m

NAME                              READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/pingponglog-dep   1/1     1            1           72m

NAME                                         DESIRED   CURRENT   READY   AGE
replicaset.apps/pingponglog-dep-5588f6b76d   0         0         0       65m
replicaset.apps/pingponglog-dep-5fffdbb574   0         0         0       20m
replicaset.apps/pingponglog-dep-65bf4986df   0         0         0       68m
replicaset.apps/pingponglog-dep-687977d8b7   0         0         0       72m
replicaset.apps/pingponglog-dep-6f6c578f8f   0         0         0       58m
replicaset.apps/pingponglog-dep-84f895d7d5   1         1         1       4m51s
replicaset.apps/pingponglog-dep-85b6f8f676   0         0         0       64m

NAME                           READY   AGE
statefulset.apps/postgres-ss   1/1     72m
(.venv)
```