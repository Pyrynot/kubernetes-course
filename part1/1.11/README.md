# Commands used:

I HATE NETWORKING I HATE NETWORKING 
I HATE NETWORKING 
I HATE NETWORKING 
I HATE NETWORKING 


Building and pushing:
```console
$ docker build -t pingpong-app:1.11 -t pyrynot/pingpong-app:1.11 -f Dockerfile.pingpong .
$ docker build -t log-output:1.11 -t pyrynot/log-output:1.11 -f Dockerfile.logoutput .

docker push pyrynot/pingpong-app:1.11
docker push pyrynot/log-output:1.11
```



Updating configs:
```console
$ kubectl apply -f manifests/
deployment.apps/pong-log-app-dep unchanged
ingress.networking.k8s.io/pong-log-app-ingress configured
persistentvolume/shared-pv unchanged
persistentvolumeclaim/shared-pvc unchanged
service/pong-log-app-svc unchanged
```


curling the address:
```console
$ curl http://localhost:8081/status
{"timestamp":"2024-08-04T11:40:41.309018","random_string":"a0f89a88-c2cb-4fb9-ac77-212eac1a9619","ping_pongs":8}(.venv) 

$ curl http://localhost:8081/pingpong
"pong 8"(.venv) 

$ curl http://localhost:8081/pingpong
"pong 9"(.venv) 

$ curl http://localhost:8081/status
{"timestamp":"2024-08-04T11:40:51.309881","random_string":"a0f89a88-c2cb-4fb9-ac77-212eac1a9619","ping_pongs":10}(.venv)
```





