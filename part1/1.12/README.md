# Commands used:



Building and pushing:
```console
$ docker build -t todo-app:1.12 -t pyrynot/todo-app:1.12 .
$ docker push pyrynot/todo-app:1.12
```

Applying configs:
```console
$ kubectl apply -f manifests/
deployment.apps/todo-app-dep unchanged
ingress.networking.k8s.io/todo-app-ingress unchanged
persistentvolume/image-cache-pv unchanged
persistentvolumeclaim/image-cache-pvc created
service/todo-app-svc unchanged
```

Making sure the image doesn't get refreshed all the time:
```console
$ kubectl logs -f todo-app-dep-6cbdc4bc69-ndw6v
INFO:     Started server process [1]
INFO:     Waiting for application startup.
Server started on port 8010
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8010 (Press CTRL+C to quit)
INFO:     10.42.1.4:51566 - "GET / HTTP/1.1" 200 OK
INFO:root:Fetching image from https://picsum.photos/1200
INFO:httpx:HTTP Request: GET https://picsum.photos/1200 "HTTP/1.1 302 Found"
INFO:httpx:HTTP Request: GET https://fastly.picsum.photos/id/688/1200/1200.jpg?hmac=XvIVnbdZCGuZo5rp46mHlY73MxBIKtnjjojuKUtPiWw "HTTP/1.1 200 OK"
INFO:root:Image saved to /app/static/image.jpg
INFO:     10.42.1.4:51566 - "GET /image HTTP/1.1" 200 OK
INFO:     10.42.1.4:51566 - "GET / HTTP/1.1" 200 OK
INFO:     10.42.1.4:51566 - "GET /image HTTP/1.1" 200 OK
INFO:     10.42.1.4:51566 - "GET / HTTP/1.1" 200 OK
INFO:     10.42.1.4:51566 - "GET /image HTTP/1.1" 200 OK
INFO:     10.42.1.4:51566 - "GET / HTTP/1.1" 200 OK
INFO:     10.42.1.4:51566 - "GET /image HTTP/1.1" 200 OK
INFO:     10.42.1.4:51566 - "GET / HTTP/1.1" 200 OK
INFO:     10.42.1.4:51566 - "GET /image HTTP/1.1" 200 OK
```

Going into the pod and creating a testfile:
```console
/app/static # ls
counter.txt  image.jpg
/app/static # touch testfile.txt
/app/static # ls
counter.txt   image.jpg     testfile.txt
/app/static # echo "Test content" > testfile.txt
/app/static # ls -l
total 140
-rw-r--r--    1 root     root             2 Aug  4 11:40 counter.txt
-rw-r--r--    1 root     root        132457 Aug  4 13:24 image.jpg
-rw-r--r--    1 root     root            13 Aug  4 13:33 testfile.txt
```

Simulating a pod restart by deleting it:
```console
$ kubectl delete pod todo-app-dep-6cbdc4bc69-6vqtw
pod "todo-app-dep-6cbdc4bc69-6vqtw" deleted

$ kubectl get pods
NAME                            READY   STATUS    RESTARTS   AGE
todo-app-dep-6cbdc4bc69-ndw6v   1/1     Running   0          28s
```

Going back to the pod to verify that the testfile exists still:
```console
/app # ls
__pycache__       config.py         image_handler.py  main.py           reqs.txt          static            templates
/app # cd static/
/app/static # ls
counter.txt   image.jpg     testfile.txt
/app/static # cat testfile.txt
Test content
```