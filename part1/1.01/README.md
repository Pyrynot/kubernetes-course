# Commands used:

(holy FUCK why haven't I heard of the autocompletion thing before??? that would've saved me tens of hours when working with Docker)

Building the image:
```console
docker build -t log-output:latest .
```

Tagging the image:
```console
docker tag log-output:latest pyrynot/log-output:latest
```

Pushing the image:
```console
docker push pyrynot/log-output:latest
```

Creating a deployment:
```console
kubectl create deployment log-output --image=pyrynot/log-output
```

Checking the deployment:
```console
$ kubectl get deployments.apps
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
log-output   1/1     1            1           2m17s
```

Making sure it's running:
```console
$ kubectl logs -f log-output-6c6454cd-n7qn2 
2024-08-03T14:45:14.540687: 3c012014-22df-4dbc-98c2-b59fbb34d8bb
2024-08-03T14:45:19.540834: 3c012014-22df-4dbc-98c2-b59fbb34d8bb
2024-08-03T14:45:24.540132: 3c012014-22df-4dbc-98c2-b59fbb34d8bb
2024-08-03T14:45:29.540313: 3c012014-22df-4dbc-98c2-b59fbb34d8bb
```