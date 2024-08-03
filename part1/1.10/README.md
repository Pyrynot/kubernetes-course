# Commands used:

Building and pushing:
```console
$ docker build -t logger:1.10 -t pyrynot/logger:1.10 -f Dockerfile.logger .
$ docker push pyrynot/logger:1.10

$ docker build -t reader:1.10 -t pyrynot/reader:1.10 -f Dockerfile.reader .
$ docker push pyrynot/reader:1.10
```

Updating configs:
```console
$ kubectl apply -f manifests/
deployment.apps/log-output-dep created
ingress.networking.k8s.io/log-output-ingress created
service/log-output-svc unchanged
```

Curling the address:
```console
$ curl http://localhost:8081
"2024-08-03T21:05:05.354738: 67754baa8da8df473c0fb0d56cf54ba7c6d765518c6f059618ffc006e64b0ea6"(.venv) 

$ curl http://localhost:8081
"2024-08-03T21:05:15.355470: 68f8b31cd18a01dccefaa22e19bc9d6b72fea2eebe0b532f2503ed599ae41a0b"(.venv) 

$ curl http://localhost:8081
"2024-08-03T21:05:20.355813: 737f9be4244861b87493d996ccaf28e6848ba2b5eccacf879bab39a0fbfb3f59"(.venv)
```