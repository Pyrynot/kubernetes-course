# Commands used:

I made a similar error here, where I hadn't separated the services into separate deployments and services. That's done now.

Editing secret:
```console
$ kubectl edit secret postgres-secret
secret/postgres-secret edited
```

Checking backend-pod:
```console
kubectl describe pod todo-backend-dep-7bdcc756fb-8gwqp 
..............................................
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
........................................................
Events:
  Type     Reason     Age                From               Message
  ----     ------     ----               ----               -------
  Normal   Scheduled  33s                default-scheduler  Successfully assigned project-namespace/todo-backend-dep-7bdcc756fb-8gwqp to k3d-k3s-default-agent-0
  Normal   Pulled     33s                kubelet            Successfully pulled image "pyrynot/todo-backend:4.02" in 1.085527173s
  Normal   Pulled     28s                kubelet            Successfully pulled image "pyrynot/todo-backend:4.02" in 948.56876ms
  Normal   Pulling    14s (x3 over 34s)  kubelet            Pulling image "pyrynot/todo-backend:4.02"
  Normal   Pulled     13s                kubelet            Successfully pulled image "pyrynot/todo-backend:4.02" in 996.544901ms
  Normal   Created    13s (x3 over 33s)  kubelet            Created container todo-backend
  Normal   Started    13s (x3 over 32s)  kubelet            Started container todo-backend
  Warning  BackOff    10s (x2 over 25s)  kubelet            Back-off restarting failed container

$ kubectl get po
NAME                                READY   STATUS    RESTARTS      AGE
postgres-ss-0                       1/1     Running   0             33m
todo-app-dep-9b966586f-4zslj        1/1     Running   0             12m
todo-backend-dep-7bdcc756fb-8gwqp   0/1     Error     1 (14s ago)   18s
```

After applying correct secret:
```console
      Liveness:   http-get http://:8000/healthz delay=10s timeout=1s period=20s #success=1 #failure=3
    Readiness:  http-get http://:8000/readyz delay=5s timeout=1s period=10s #success=1 #failure=3
```

Checking pods: (bug in the cronjob has been fixed)
```console
$ kubectl get po
NAME                                      READY   STATUS             RESTARTS        AGE
postgres-ss-0                             1/1     Running            0               41m
todo-app-dep-9b966586f-4zslj              1/1     Running            0               19m
todo-backend-dep-7bdcc756fb-8gwqp         1/1     Running            5 (6m18s ago)   8m
random-todo-generator-28721760--1-dqsnc   0/1     CrashLoopBackOff   4 (49s ago)     2m26s
```