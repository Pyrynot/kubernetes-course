# Commands used:


Retagging:
```console
docker tag log-output:latest pyrynot/log-output:1.03
```

Re-pushing with correct tag:
```console
docker push pyrynot/log-output:1.03
```

Creating a deployment with the yaml:
```console
$ kubectl apply -f manifests/deployment.yaml
deployment.apps/log-output created
```

Checking deps:
```console
$ kubectl get deployments.apps
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
log-output   1/1     1            1           6s
```

Looking at logs to make sure it works:
```console
$ kubectl logs -f log-output-95668494d-xtprs
2024-08-03T16:05:24.575962: b1c529e7-c649-4d6b-ad7e-7ae97d3bb82c
2024-08-03T16:05:29.576166: b1c529e7-c649-4d6b-ad7e-7ae97d3bb82c
2024-08-03T16:05:34.576348: b1c529e7-c649-4d6b-ad7e-7ae97d3bb82c
```


