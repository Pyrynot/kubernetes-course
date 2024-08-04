# Commands used:


Secret for database_url and database_password
```console
$ kubectl apply -f manifests/secret.yaml
secret/postgres-secret created
```

Getting base64 for the connection string:
```console
$ echo -n 'postgresql+psycopg2://postgres:XXXXXXXX@postgres-svc:5432/postgres' | base64
cG9zdGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXJlcy1zdmM6
NTQzMi9wb3N0Z3Jlcw==
```



Curling to check if everything works:
```console
$ curl http://localhost:8081/
{"file content":"this text is from file","env variable":"hello world","log":"2024-08-04T20:49:39.961995: 4673e4c70da95d3b1ebbdf502dded2db2b1b9cc2e3d4f892a6290d8f0e567541. Ping / Pongs: 10"}(.venv) 

$ curl http://localhost:8081/pingpong
"pong 11"(.venv) 

$ curl http://localhost:8081/
{"file content":"this text is from file","env variable":"hello world","log":"2024-08-04T20:49:55.045706: 7c88cd70012a4af560555e8a7ff6bb4fb4e0893ea6a2d38866860cca414b9231. Ping / Pongs: 11"}(.venv) 
```


Deleting all pods to see if the data persists:
```console
$ curl http://localhost:8081/pingpong
"pong 12"(.venv) 

$ kubectl get pods
NAME                               READY   STATUS    RESTARTS   AGE
postgres-ss-0                      1/1     Running   0          8m47s
pingponglog-dep-8447c8f5f7-576qs   3/3     Running   0          6m43s
(.venv) 

$ kubectl delete pods --all -n exercise-namespace
pod "postgres-ss-0" deleted
pod "pingponglog-dep-8447c8f5f7-576qs" deleted
(.venv) 

$ kubectl get pods -n exercise-namespace
NAME                               READY   STATUS    RESTARTS   AGE
postgres-ss-0                      1/1     Running   0          19s
pingponglog-dep-8447c8f5f7-dl4db   3/3     Running   0          19s
(.venv) 

$ curl http://localhost:8081/pingpong
"pong 13"(.venv) 
```