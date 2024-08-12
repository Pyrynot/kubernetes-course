# Commands used



Applying changes:
```console
$ kustomizeapply
configmap/pingponglog-configmap unchanged
secret/postgres-secret unchanged
Warning: Kubernetes default value is insecure, Knative may default this to secure in a future release: spec.template.spec.containers[0].securityContext.allowPrivilegeEscalation, spec.template.spec.containers[0].securityContext.capabilities, spec.template.spec.containers[0].securityContext.runAsNonRoot, spec.template.spec.containers[0].securityContext.seccompProfile
service.serving.knative.dev/pingpong-knative created
service/postgres-svc created
statefulset.apps/postgres-ss created
(.venv)
```

Checking pod logs:
```console
$ kubectl logs pingpong-knative-00001-deployment-75cd7975df-7zv99 
Defaulted container "user-container" out of: user-container, queue-proxy
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     127.0.0.1:55736 - "GET /pingpong/healthz HTTP/1.1" 200 OK
INFO:     127.0.0.1:51256 - "GET /pingpong/healthz HTTP/1.1" 200 OK
INFO:     127.0.0.1:41060 - "GET /pingpong/healthz HTTP/1.1" 200 OK
INFO:     127.0.0.1:42132 - "GET /pingpong/healthz HTTP/1.1" 200 OK
INFO:     127.0.0.1:59040 - "GET /pingpong/healthz HTTP/1.1" 200 OK
INFO:     127.0.0.1:48212 - "GET /pingpong/healthz HTTP/1.1" 200 OK
INFO:     127.0.0.1:45010 - "GET /pingpong/healthz HTTP/1.1" 200 OK
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [1]
(.venv) 
```

Getting ksvc:
```console
$ kubectl get ksvc
NAME               URL                                                      LATESTCREATED            LATESTREADY              READY   REASON
pingpong-knative   http://pingpong-knative.exercise-namespace.example.com   pingpong-knative-00002   pingpong-knative-00002   True
(.venv)
```

Curling the pingpong app:
```console
$ curl H -"Host: pingpong-knative.exercise-namespace.example.com" http://localhost:8081
curl: (6) Could not resolve host: H
(.venv)

$ curl -H "Host: pingpong-knative.exercise-namespace.example.com" http://localhost:8081
{"message":"Service is up and running"}(.venv)

$ curl -H "Host: pingpong-knative.exercise-namespace.example.com" http://localhost:8081/pingpong
"pong 1"(.venv)

$ curl -H "Host: pingpong-knative.exercise-namespace.example.com" http://localhost:8081/pingpong
"pong 2"(.venv)

$ curl -H "Host: pingpong-knative.exercise-namespace.example.com" http://localhost:8081/pingpong
"pong 3"(.venv)

$ curl -H "Host: pingpong-knative.exercise-namespace.example.com" http://localhost:8081/pingpong
"pong 4"(.venv)

$ curl -H "Host: pingpong-knative.exercise-namespace.example.com" http://localhost:8081/pingpong
"pong 5"(.venv)
```