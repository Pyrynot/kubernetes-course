# Commands used:



Building and pushing:
```console
docker compose build
docker compose push
```

Applying configs:
```console
$ kubectl apply -f manifests/
deployment.apps/pingponglog-dep configured
ingress.networking.k8s.io/pingponglog-ingress unchanged
service/pingponglog-svc unchanged
```

Curling the addresses:
```console
$ curl http://localhost:8081/
{"log":"2024-08-04T15:40:40.583331: bdaa1a6c86baca8784709fc72e4df32b82a28e647ba6cad2c70bc3e67310d7f2. Ping / Pongs: 0"}(.venv) 

$ curl http://localhost:8081/pingpong
"pong 1"(.venv) 

$ curl http://localhost:8081/latest_log
{"log":"2024-08-04T15:41:00.664628: 642f6912733f4443efbb80bbd006bec737fad8670d8ccb94809e15caf0ea7bf8. Ping / Pongs: 1"}(.venv) 

$ curl http://localhost:8081/
{"log":"2024-08-04T15:41:05.684926: fc19f4a918447778528ced21c436c9bcce74ac3acc98e3f0efbead8bca4b43fd. Ping / Pongs: 1"}(.venv) 
```