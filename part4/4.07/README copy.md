# Commands used:

## Oopsie, I hadn't realized that I was supposed to split these into 2 deployments. Makes sense tbh.

## kustomizeapply is an alias for:
```console
kustomize build . | kubectl apply -f -
```

Apply without statefulset.yaml:
```console
heino@Pyrre MINGW64 /c/Users/heino/Code/kubernetes-course/part4/4.01 (main)
$ kustomizeapply
configmap/pingponglog-configmap unchanged
secret/postgres-secret unchanged
service/logoutput-svc created
service/pingpong-svc created
service/postgres-svc created
deployment.apps/logoutput-dep created
deployment.apps/pingpong-dep created
ingress.networking.k8s.io/pingponglog-ingress unchanged
```

Check pods:
```console
$ kubectl get pods
NAME                            READY   STATUS    RESTARTS      AGE
logoutput-dep-8cbc4495c-hhp9p   1/2     Running   0             16s
pingpong-dep-5c6cdbd6c9-rrmmp   0/1     Error     1 (12s ago)   16s
```

Apply statefulset.yaml:
```console
$ kubectl apply -f manifests/statefulset.yaml
statefulset.apps/postgres-ss created
```

Check pods:
```console
$ kubectl get pods
NAME                            READY   STATUS    RESTARTS      AGE
postgres-ss-0                   1/1     Running   0             30s
pingpong-dep-5c6cdbd6c9-rrmmp   1/1     Running   2 (45s ago)   53s
logoutput-dep-8cbc4495c-hhp9p   2/2     Running   0             53s
```


Check logs:

```console
$ kubectl logs logoutput-dep-8cbc4495c-hhp9p 
Defaulted container "logger" out of: logger, reader
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     10.42.2.1:36906 - "GET /logger/healthz HTTP/1.1" 500 Internal Server Error
INFO:     10.42.2.1:36914 - "GET /logger/healthz HTTP/1.1" 500 Internal Server Error
INFO:     10.42.2.1:50268 - "GET /logger/healthz HTTP/1.1" 500 Internal Server Error
INFO:     10.42.2.1:50284 - "GET /logger/healthz HTTP/1.1" 500 Internal Server Error
INFO:     10.42.2.1:56752 - "GET /logger/healthz HTTP/1.1" 500 Internal Server Error
2024-08-10T14:53:23.745942: efe6305550f9e32c9e022089f91c4f70a18da3b0d247920edf056c2c2303aa08. Ping / Pongs: 11
INFO:     10.42.2.1:56762 - "GET /logger/healthz HTTP/1.1" 200 OK
2024-08-10T14:53:28.771010: 43247dc79ea954d12ed92b27f25af13cc7b55788a3b8d895a9c96f9ab2c7f4e8. Ping / Pongs: 11
INFO:     10.42.2.1:55572 - "GET /logger/healthz HTTP/1.1" 200 OK
```