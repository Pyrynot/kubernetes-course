# Current project:


Importing image to local:
```console
k3d image import pyrynot/todo-backend:2.08
```

Applying:
```console
$ kubectl apply -f manifests/
deployment.apps/todo-app-dep created
ingress.networking.k8s.io/todo-app-ingress created
service/postgres-svc created
persistentvolume/image-cache-pv unchanged
persistentvolumeclaim/image-cache-pvc created
secret/postgres-secret created
service/todo-app-svc created
statefulset.apps/postgres-ss created
(.venv) 
```

Curling address:
```console
$ curl http://localhost:8081/todos
[{"content":"SKrrtt"},{"content":"sdfsdf"}](.venv) 

$ curl -X POST "http://localhost:8081/todos" -H "Content-Type: application/json" -d '{"content": "Test 123"}'
{"content":"Test 123"}(.venv) 

$ curl http://localhost:8081/todos
[{"content":"SKrrtt"},{"content":"sdfsdf"},{"content":"Test 123"}](.venv) 

```


Checking the postgres shell:
```console
psql (13.0 (Debian 13.0-1.pgdg100+1))
Type "help" for help.

postgres=# \dt
         List of relations
 Schema | Name  | Type  |  Owner
--------+-------+-------+----------
 public | todos | table | postgres
(1 row)

postgres=# SELECT * FROM todos;
 id | content
----+----------
  1 | SKrrtt
  2 | sdfsdf
  3 | Test 123
(3 rows)

postgres=#
```