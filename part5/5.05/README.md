# Commands used


Applying the example:
```console
$ kubectl apply -f hello.yaml
Warning: Kubernetes default value is insecure, Knative may default this to secure in a future release: spec.template.spec.containers[0].securityContext.allowPrivilegeEscalation, spec.template.spec.containers[0].securityContext.capabilities, spec.template.spec.containers[0].securityContext.runAsNonRoot, spec.template.spec.containers[0].securityContext.seccompProfile
service.serving.knative.dev/hello created
```

Going the NoDNS route:
```console
$ kubectl get ksvc
NAME    URL                                LATESTCREATED   LATESTREADY   READY   REASON
hello   http://hello.default.example.com   hello-00001     hello-00001   True
```

Accessing the service:
```console
$ curl -H "Host: hello.default.example.com" http://localhost:8081
Hello World!
```

Checking autoscaling:
```console
$ kubectl get pod -l serving.knative.dev/service=hello -w
NAME                                      READY   STATUS    RESTARTS   AGE
hello-00001-deployment-5b79fc648b-6gqpb   0/2     Pending   0          0s
hello-00001-deployment-5b79fc648b-6gqpb   0/2     Pending   0          0s
hello-00001-deployment-5b79fc648b-6gqpb   0/2     ContainerCreating   0          0s
hello-00001-deployment-5b79fc648b-6gqpb   1/2     Running             0          2s
hello-00001-deployment-5b79fc648b-6gqpb   2/2     Running             0          2s
```

Applying new example:
```console
$ kubectl apply -f hello.yaml
Warning: Kubernetes default value is insecure, Knative may default this to secure in a future release: spec.template.spec.containers[0].securityContext.allowPrivilegeEscalation, spec.template.spec.containers[0].securityContext.capabilities, spec.template.spec.containers[0].securityContext.runAsNonRoot, spec.template.spec.containers[0].securityContext.seccompProfile
service.serving.knative.dev/hello configured
(.venv) 
```

Accessing app again:
```console
$ curl -H "Host: hello.default.example.com" http://localhost:8081
Hello Knative!
(.venv) 
```

Checking revisions:
```console
$ kubectl get revisions
NAME          CONFIG NAME   GENERATION   READY   REASON   ACTUAL REPLICAS   DESIRED REPLICAS
hello-00001   hello         1            True             0                 0
hello-00002   hello         2            True             1                 1
(.venv) 
```

Example with traffic:
```console
$ kubectl apply -f hello.yaml
Warning: Kubernetes default value is insecure, Knative may default this to secure in a future release: spec.template.spec.containers[0].securityContext.allowPrivilegeEscalation, spec.template.spec.containers[0].securityContext.capabilities, spec.template.spec.containers[0].securityContext.runAsNonRoot, spec.template.spec.containers[0].securityContext.seccompProfile
service.serving.knative.dev/hello configured
(.venv) 
```

Discovering that this doesn't show the traffic:
```console
$ kubectl get revisions
NAME          CONFIG NAME   GENERATION   READY   REASON   ACTUAL REPLICAS   DESIRED REPLICAS
hello-00001   hello         1            True             0                 0
hello-00002   hello         2            True             1                 1
```