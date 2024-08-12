# Commands used

Pushing manually (shudder):
```console
docker build -t pyrynot/dummysite-controller:1.0 .

docker push pyrynot/dummysite-controller:1.0
```

Applying:
```console
kubectl apply -f dummysite_crd.yaml
kubectl apply -f rbac.yaml
kubectl apply -f controller_deployment.yaml
```

Creating dummysite:
```console
heino@Pyrre MINGW64 /c/Users/heino/Code/kubernetes-course/part5/5.01 (main)
$ kubectl apply -f test_dummysite.yaml
dummysite.example.com/example-site created
```

Checking pods:
```console
$ kubectl get po
NAME                                   READY   STATUS    RESTARTS   AGE
dummysite-controller-9955cd5bf-vnhgq   1/1     Running   0          4m47s
example-site-pod                       1/1     Running   0          4m2s
```

Checking pod logs:
```console
$ kubectl logs example-site-pod 
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2024/08/12 15:12:24 [notice] 1#1: using the "epoll" event method
2024/08/12 15:12:24 [notice] 1#1: nginx/1.27.0
2024/08/12 15:12:24 [notice] 1#1: built by gcc 13.2.1 20231014 (Alpine 13.2.1_git20231014) 
2024/08/12 15:12:24 [notice] 1#1: OS: Linux 5.15.153.1-microsoft-standard-WSL2
2024/08/12 15:12:24 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2024/08/12 15:12:24 [notice] 1#1: start worker processes
2024/08/12 15:12:24 [notice] 1#1: start worker process 30
2024/08/12 15:12:24 [notice] 1#1: start worker process 31
2024/08/12 15:12:24 [notice] 1#1: start worker process 32
2024/08/12 15:12:24 [notice] 1#1: start worker process 33
2024/08/12 15:12:24 [notice] 1#1: start worker process 34
2024/08/12 15:12:24 [notice] 1#1: start worker process 35
2024/08/12 15:12:24 [notice] 1#1: start worker process 36
2024/08/12 15:12:24 [notice] 1#1: start worker process 37
2024/08/12 15:12:24 [notice] 1#1: start worker process 38
2024/08/12 15:12:24 [notice] 1#1: start worker process 39
2024/08/12 15:12:24 [notice] 1#1: start worker process 40
2024/08/12 15:12:24 [notice] 1#1: start worker process 41
2024/08/12 15:12:24 [notice] 1#1: start worker process 42
2024/08/12 15:12:24 [notice] 1#1: start worker process 43
2024/08/12 15:12:24 [notice] 1#1: start worker process 44
2024/08/12 15:12:24 [notice] 1#1: start worker process 45


Checking controller logs:
```console
$ kubectl logs dummysite-controller-9955cd5bf-vnhgq 
/usr/local/lib/python3.9/site-packages/kopf/_core/reactor/running.py:179: FutureWarning: Absence of either namespaces or cluster-wide flag will become an error soon. For now, switching to the cluster-wide mode for backward compatibility.
  warnings.warn("Absence of either namespaces or cluster-wide flag will become an error soon."
[2024-08-12 15:11:40,492] kopf._core.engines.a [INFO    ] Initial authentication has been initiated.
[2024-08-12 15:11:40,494] kopf.activities.auth [INFO    ] Activity 'login_via_client' succeeded.
[2024-08-12 15:11:40,495] kopf._core.engines.a [INFO    ] Initial authentication has finished.
[2024-08-12 15:11:40,512] kopf._core.reactor.o [WARNING ] Not enough permissions to watch for resources: changes (creation/deletion/updates) will not be noticed; the resources are only refreshed on operator restarts.
[2024-08-12 15:12:23,731] kopf.objects         [INFO    ] [project-namespace/example-site] Handler 'create_dummysite' succeeded.
[2024-08-12 15:12:23,732] kopf.objects         [INFO    ] [project-namespace/example-site] Creation is processed: 1 succeeded; 0 failed.
[2024-08-12 15:12:23,746] kopf.objects         [WARNING ] [project-namespace/example-site] Patching failed with inconsistencies: (('remove', ('status',), {'create_dummysite': {'message': 'DummySite resources created successfully'}}, None),)
```

Trying to troubleshoot why port-forward doesn't work:
```console
$ kubectl describe pod example-site-pod 
Name:             example-site-pod
Namespace:        project-namespace
Priority:         0
Service Account:  default
Node:             k3d-k3s-default-agent-0/172.31.0.5
Start Time:       Mon, 12 Aug 2024 18:12:23 +0300
Labels:           <none>
Annotations:      <none>
Status:           Running
IP:               10.42.2.243
IPs:
  IP:  10.42.2.243
Containers:
  nginx:
    Container ID:   containerd://23efddede649833813b31be5b117a7739259fc99600ce49fcab99c65adf18431
    Image:          nginx:alpine
    Image ID:       docker.io/library/nginx@sha256:208b70eefac13ee9be00e486f79c695b15cef861c680527171a27d253d834be9
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Mon, 12 Aug 2024 18:12:24 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /usr/share/nginx/html from content (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-79ljt (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  content:
    Type:      ConfigMap (a volume populated by a ConfigMap)
    Name:      example-site-content
    Optional:  false
  kube-api-access-79ljt:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  4m24s  default-scheduler  Successfully assigned project-namespace/example-site-pod to k3d-k3s-default-agent-0
  Normal  Pulled     4m24s  kubelet            Container image "nginx:alpine" already present on machine
  Normal  Created    4m24s  kubelet            Created container nginx
  Normal  Started    4m24s  kubelet            Started container nginx
```

Describing service:
```console
$ kubectl describe svc example-site-service 
Name:              example-site-service
Namespace:         project-namespace
Labels:            <none>
Annotations:       <none>
Selector:          app=example-site-pod
Type:              ClusterIP
IP Family Policy:  SingleStack
IP Families:       IPv4
IP:                10.43.65.49
IPs:               10.43.65.49
Port:              <unset>  80/TCP
TargetPort:        80/TCP
Endpoints:         <none>
Session Affinity:  None
Events:            <none>
```

No endpoints:
```console
$ kubectl get endpoints example-site-service 
NAME                   ENDPOINTS   AGE
example-site-service   <none>      5m21s
```


Labeling the pod so the service connects to it:
```console
$ kubectl label pod example-site-pod app=example-site-pod -n project-namespace
pod/example-site-pod labeled
```

Checking endpoints again:
```console
$ kubectl get endpoints example-site-service 
NAME                   ENDPOINTS        AGE
example-site-service   10.42.2.243:80   10m

Port-forward works now:
```console
$ kubectl port-forward service/example-site-service 8080:80
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
Handling connection for 8080
Handling connection for 8080
Handling connection for 8080
Handling connection for 8080
```


Curling the dummysite:
```console
$ curl http://localhost:8080
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0<!DOCTYPE html>
<html class="client-nojs sse-other" lang="fi" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>Kunnossa impattuaan varmaan 100 tuntiakin impattuaan | Kopiopasta Wiki | Fandom</title>
<script>document.documentElement.className="client-js sse-other";RLCONF={"wgBreakFrames":false,"wgSeparatorTransformTable":[",\t."," \t,"],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"fi normal",

..................................................................

<meta name="format-detection" content="telephone=no"/>
<meta name="description" content="Ite oon impannut yhteensä varmaan kymmeniä tunteja ja oon 100% kunnossa vaikka oon impaanut varmaan 100 tuntiakin impannut"/>
<meta name="twitter:card" content="summary"/>
<meta name="twitter:site" content="@getfandom"/>
<meta name="twitter:url" content="https://kopiopasta.fandom.com/fi/wiki/Kunnossa_impattuaan_varmaan_100_tuntiakin_impattuaan"/>
<meta name="twitter:title" content="Kunnossa impattuaan varmaan 100 tuntiakin impattuaan | Kopiopasta..."/>
<meta name="twitter:description" content="Ite oon impannut yhteensä varmaan kymmeniä tunteja ja oon 100% kunnossa vaikka oon impaanut varmaan 100 tuntiakin impannut"/>

.................................................................

<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgPageParseReport":{"limitreport":{"cputime":"0.001","walltime":"0.001","ppvisitednodes":{"value":1,"limit":1000000},"postexpandincludesize":{"value":0,"limit":2097152},"templateargumentsize":{"value":0,"limit":2097152},"expansiondepth":{"value":1,"limit":100},"expensivefunctioncount":{"value":0,"limit":100},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":0,"limit":5000000},"timingprofile":["100.00%    0.000      1 -total"]},"cachereport":{"timestamp":"20240807070502","ttl":1209600,"transientcontent":false}}});});</script>
<script defer="" src="https://www.fastly-insights.com/static/scout.js?k=17272cd8100  104k  100  104k    0     0  12.3M      0 --:--:-- --:--:-- --:--:-- 12.7Mb5-b5a3-b3cd5403f7c5"></script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgBackendResponseTime":94});});</script>
</body>
</html>
```

Curling the example site:
```console
$ curl http://localhost:8080
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0   168k      0 --:--:-- --:--:-- --:--:--  175k<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
```