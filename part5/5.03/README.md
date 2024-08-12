```console
$ kubectl apply -k github.com/fluxcd/flagger/kustomize/linkerd
# Warning: 'bases' is deprecated. Please use 'resources' instead. Run 'kustomize edit fix' to update your Kustomization automatically.
# Warning: 'patchesJson6902' is deprecated. Please use 'patches' instead. Run 'kustomize edit fix' to update your Kustomization automatically.
# Warning: 'patchesStrategicMerge' is deprecated. Please use 'patches' instead. Run 'kustomize edit fix' to update your Kustomization automatically.
namespace/flagger-system created
customresourcedefinition.apiextensions.k8s.io/alertproviders.flagger.app created
customresourcedefinition.apiextensions.k8s.io/canaries.flagger.app created
customresourcedefinition.apiextensions.k8s.io/metrictemplates.flagger.app created
serviceaccount/flagger created
clusterrole.rbac.authorization.k8s.io/flagger created
clusterrolebinding.rbac.authorization.k8s.io/flagger created
deployment.apps/flagger created
authorizationpolicy.policy.linkerd.io/prometheus-admin-flagger created
(.venv) 

$ kubectl -n flagger-system rollout status deploy/flagger
deployment "flagger" successfully rolled out
(.venv) 

$ kubectl create ns test && \
  kubectl apply -f https://run.linkerd.io/flagger.yml
namespace/test created
deployment.apps/load created
configmap/frontend created
deployment.apps/frontend created
service/frontend created
deployment.apps/podinfo created
service/podinfo created
(.venv) 

$ kubectl -n test rollout status deploy podinfo
Waiting for deployment "podinfo" rollout to finish: 0 of 1 updated replicas are available...
deployment "podinfo" successfully rolled out
(.venv) 

$ kubectl -n test port-forward svc/frontend 8080
Forwarding from 127.0.0.1:8080 -> 8080
Forwarding from [::1]:8080 -> 8080
Handling connection for 8080

(.venv) 
$ kubectl apply -f - <<EOF
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: podinfo
  namespace: test
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: podinfo
  service:
    # service port number
    port: 9898
    # container port number or name (optional)
    targetPort: 9898
    # Reference to the Service that the generated HTTPRoute would attach to.
    gatewayRefs:
      - name: podinfo
        namespace: test
        group: core
        kind: Service
        port: 9898
  analysis:
    interval: 10s
    threshold: 5
    stepWeight: 10
    maxWeight: 100
    metrics:
    - name: success-rate
      templateRef:
        name: success-rate
        namespace: test
EOF * 100[{{ interval }}]und"get }}",,-viz:9090
canary.flagger.app/podinfo created
metrictemplate.flagger.app/success-rate created
(.venv) 

$ kubectl -n test get ev --watch
Warning: short name "ev" could also match lower priority resource events.events.k8s.io
LAST SEEN   TYPE      REASON                  OBJECT                           MESSAGE
44s         Normal    ScalingReplicaSet       deployment/load                  Scaled up replica set load-7f97579865 to 1
44s         Normal    Injected                deployment/load                  Linkerd sidecar proxy injected
44s         Normal    ScalingReplicaSet       deployment/frontend              Scaled up replica set frontend-6957977dc7 to 1
44s         Normal    SuccessfulCreate        replicaset/load-7f97579865       Created pod: load-7f97579865-kbm2h
43s         Normal    Scheduled               pod/load-7f97579865-kbm2h        Successfully assigned test/load-7f97579865-kbm2h to k3d-k3s-default-agent-1
44s         Normal    Injected                deployment/frontend              Linkerd sidecar proxy injected
43s         Normal    SuccessfulCreate        replicaset/frontend-6957977dc7   Created pod: frontend-6957977dc7-m7czk
43s         Normal    Scheduled               pod/frontend-6957977dc7-m7czk    Successfully assigned test/frontend-6957977dc7-m7czk to k3d-k3s-default-server-0
43s         Normal    ScalingReplicaSet       deployment/podinfo               Scaled up replica set podinfo-7bfd46f477 to 1
43s         Normal    Injected                deployment/podinfo               Linkerd sidecar proxy injected
43s         Normal    SuccessfulCreate        replicaset/podinfo-7bfd46f477    Created pod: podinfo-7bfd46f477-twbm7
43s         Normal    Scheduled               pod/podinfo-7bfd46f477-twbm7     Successfully assigned test/podinfo-7bfd46f477-twbm7 to k3d-k3s-default-agent-0
43s         Normal    Pulled                  pod/load-7f97579865-kbm2h        Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
43s         Normal    Created                 pod/load-7f97579865-kbm2h        Created container linkerd-init
43s         Normal    Pulled                  pod/podinfo-7bfd46f477-twbm7     Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
43s         Normal    Started                 pod/load-7f97579865-kbm2h        Started container linkerd-init
43s         Normal    Created                 pod/podinfo-7bfd46f477-twbm7     Created container linkerd-init
43s         Normal    Started                 pod/podinfo-7bfd46f477-twbm7     Started container linkerd-init
42s         Normal    Pulled                  pod/podinfo-7bfd46f477-twbm7     Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
42s         Normal    Created                 pod/podinfo-7bfd46f477-twbm7     Created container linkerd-proxy
42s         Warning   FailedMount             pod/frontend-6957977dc7-m7czk    MountVolume.SetUp failed for volume "cfg" : failed to sync configmap cache: timed out waiting for the condition
42s         Normal    Started                 pod/podinfo-7bfd46f477-twbm7     Started container linkerd-proxy
42s         Normal    IssuedLeafCertificate   serviceaccount/default           issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:02 +0000 UTC: dff1b169e1bc4dd55c68f72ea36acbb17838d04b7e5cb72fd0f98ce48035cce1
42s         Normal    Pulling                 pod/podinfo-7bfd46f477-twbm7     Pulling image "quay.io/stefanprodan/podinfo:1.7.0"
42s         Normal    Pulled                  pod/load-7f97579865-kbm2h        Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
42s         Normal    Created                 pod/load-7f97579865-kbm2h        Created container linkerd-proxy
42s         Normal    Started                 pod/load-7f97579865-kbm2h        Started container linkerd-proxy
41s         Normal    IssuedLeafCertificate   serviceaccount/default           issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:03 +0000 UTC: b7239570dbabc4ecb62d046413c1e9e1f6259033a10ce473a29c0ec47ed2ce1e
41s         Normal    Pulled                  pod/load-7f97579865-kbm2h        Container image "buoyantio/slow_cooker:1.2.0" already present on machine
41s         Normal    Created                 pod/load-7f97579865-kbm2h        Created container slow-cooker
41s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
41s         Normal    Started                 pod/load-7f97579865-kbm2h        Started container slow-cooker
41s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-init
41s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container linkerd-init
40s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
40s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-proxy
42s         Normal    Started                 pod/podinfo-7bfd46f477-twbm7     Started container linkerd-proxy
42s         Normal    IssuedLeafCertificate   serviceaccount/default           issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:02 +0000 UTC: dff1b169e1bc4dd55c68f72ea36acbb17838d04b7e5cb72fd0f98ce48035cce1
42s         Normal    Pulling                 pod/podinfo-7bfd46f477-twbm7     Pulling image "quay.io/stefanprodan/podinfo:1.7.0"
42s         Normal    Pulled                  pod/load-7f97579865-kbm2h        Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
42s         Normal    Created                 pod/load-7f97579865-kbm2h        Created container linkerd-proxy
42s         Normal    Started                 pod/load-7f97579865-kbm2h        Started container linkerd-proxy
41s         Normal    IssuedLeafCertificate   serviceaccount/default           issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:03 +0000 UTC: b7239570dbabc4ecb62d046413c1e9e1f6259033a10ce473a29c0ec47ed2ce1e
41s         Normal    Pulled                  pod/load-7f97579865-kbm2h        Container image "buoyantio/slow_cooker:1.2.0" already present on machine
41s         Normal    Created                 pod/load-7f97579865-kbm2h        Created container slow-cooker
41s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
41s         Normal    Started                 pod/load-7f97579865-kbm2h        Started container slow-cooker
41s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-init
41s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container linkerd-init
40s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
40s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-proxy
42s         Normal    IssuedLeafCertificate   serviceaccount/default           issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:02 +0000 UTC: dff1b169e1bc4dd55c68f72ea36acbb17838d04b7e5cb72fd0f98ce48035cce1
42s         Normal    Pulling                 pod/podinfo-7bfd46f477-twbm7     Pulling image "quay.io/stefanprodan/podinfo:1.7.0"
42s         Normal    Pulled                  pod/load-7f97579865-kbm2h        Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
42s         Normal    Created                 pod/load-7f97579865-kbm2h        Created container linkerd-proxy
42s         Normal    Started                 pod/load-7f97579865-kbm2h        Started container linkerd-proxy
41s         Normal    IssuedLeafCertificate   serviceaccount/default           issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:03 +0000 UTC: b7239570dbabc4ecb62d046413c1e9e1f6259033a10ce473a29c0ec47ed2ce1e
41s         Normal    Pulled                  pod/load-7f97579865-kbm2h        Container image "buoyantio/slow_cooker:1.2.0" already present on machine
41s         Normal    Created                 pod/load-7f97579865-kbm2h        Created container slow-cooker
41s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
41s         Normal    Started                 pod/load-7f97579865-kbm2h        Started container slow-cooker
41s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-init
41s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container linkerd-init
40s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
40s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-proxy
42s         Normal    Pulled                  pod/load-7f97579865-kbm2h        Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
42s         Normal    Created                 pod/load-7f97579865-kbm2h        Created container linkerd-proxy
42s         Normal    Started                 pod/load-7f97579865-kbm2h        Started container linkerd-proxy
41s         Normal    IssuedLeafCertificate   serviceaccount/default           issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:03 +0000 UTC: b7239570dbabc4ecb62d046413c1e9e1f6259033a10ce473a29c0ec47ed2ce1e
41s         Normal    Pulled                  pod/load-7f97579865-kbm2h        Container image "buoyantio/slow_cooker:1.2.0" already present on machine
41s         Normal    Created                 pod/load-7f97579865-kbm2h        Created container slow-cooker
41s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
41s         Normal    Started                 pod/load-7f97579865-kbm2h        Started container slow-cooker
41s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-init
41s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container linkerd-init
40s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
40s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-proxy
41s         Normal    IssuedLeafCertificate   serviceaccount/default           issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:03 +0000 UTC: b7239570dbabc4ecb62d046413c1e9e1f6259033a10ce473a29c0ec47ed2ce1e
41s         Normal    Pulled                  pod/load-7f97579865-kbm2h        Container image "buoyantio/slow_cooker:1.2.0" already present on machine
41s         Normal    Created                 pod/load-7f97579865-kbm2h        Created container slow-cooker
41s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
41s         Normal    Started                 pod/load-7f97579865-kbm2h        Started container slow-cooker
41s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-init
41s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container linkerd-init
40s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
40s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-proxy
41s         Normal    Created                 pod/load-7f97579865-kbm2h        Created container slow-cooker
41s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
41s         Normal    Started                 pod/load-7f97579865-kbm2h        Started container slow-cooker
41s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-init
41s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container linkerd-init
40s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
40s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-proxy
40s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container linkerd-proxy
40s         Normal    IssuedLeafCertificate   serviceaccount/default           issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:04 +0000 UTC: 3e1b0fb8e147e90660266ca953aea49f2e120ef98a854078a78bc130477060b1
41s         Normal    Started                 pod/load-7f97579865-kbm2h        Started container slow-cooker
41s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-init
41s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container linkerd-init
40s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
40s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-proxy
40s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container linkerd-proxy
40s         Normal    IssuedLeafCertificate   serviceaccount/default           issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:04 +0000 UTC: 3e1b0fb8e147e90660266ca953aea49f2e120ef98a854078a78bc130477060b1
40s         Normal    Pulling                 pod/frontend-6957977dc7-m7czk    Pulling image "nginx:alpine"
40s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container linkerd-proxy
40s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container linkerd-proxy
40s         Normal    IssuedLeafCertificate   serviceaccount/default           issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:04 +0000 UTC: 3e1b0fb8e147e90660266ca953aea49f2e120ef98a854078a78bc130477060b1
40s         Normal    Pulling                 pod/frontend-6957977dc7-m7czk    Pulling image "nginx:alpine"
39s         Normal    Pulled                  pod/podinfo-7bfd46f477-twbm7     Successfully pulled image "quay.io/stefanprodan/podinfo:1.7.0" in 2.947361578s
40s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container linkerd-proxy
40s         Normal    IssuedLeafCertificate   serviceaccount/default           issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:04 +0000 UTC: 3e1b0fb8e147e90660266ca953aea49f2e120ef98a854078a78bc130477060b1
40s         Normal    Pulling                 pod/frontend-6957977dc7-m7czk    Pulling image "nginx:alpine"
39s         Normal    Pulled                  pod/podinfo-7bfd46f477-twbm7     Successfully pulled image "quay.io/stefanprodan/podinfo:1.7.0" in 2.947361578s
40s         Normal    Pulling                 pod/frontend-6957977dc7-m7czk    Pulling image "nginx:alpine"
39s         Normal    Pulled                  pod/podinfo-7bfd46f477-twbm7     Successfully pulled image "quay.io/stefanprodan/podinfo:1.7.0" in 2.947361578s
39s         Normal    Created                 pod/podinfo-7bfd46f477-twbm7     Created container podinfod
39s         Normal    Started                 pod/podinfo-7bfd46f477-twbm7     Started container podinfod
39s         Normal    Pulled                  pod/podinfo-7bfd46f477-twbm7     Successfully pulled image "quay.io/stefanprodan/podinfo:1.7.0" in 2.947361578s
39s         Normal    Created                 pod/podinfo-7bfd46f477-twbm7     Created container podinfod
39s         Normal    Started                 pod/podinfo-7bfd46f477-twbm7     Started container podinfod
36s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Successfully pulled image "nginx:alpine" in 4.249071928s
39s         Normal    Created                 pod/podinfo-7bfd46f477-twbm7     Created container podinfod
39s         Normal    Started                 pod/podinfo-7bfd46f477-twbm7     Started container podinfod
36s         Normal    Pulled                  pod/frontend-6957977dc7-m7czk    Successfully pulled image "nginx:alpine" in 4.249071928s
36s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container nginx
36s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container nginx
36s         Normal    Created                 pod/frontend-6957977dc7-m7czk    Created container nginx
36s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container nginx
36s         Normal    Started                 pod/frontend-6957977dc7-m7czk    Started container nginx
0s          Normal    Synced                  canary/podinfo                   all the metrics providers are available!
0s          Warning   Synced                  canary/podinfo                   podinfo-primary.test not ready: waiting for rollout to finish: observed deployment generation less than desired generation
0s          Normal    Synced                  canary/podinfo                   all the metrics providers are available!
0s          Warning   Synced                  canary/podinfo                   podinfo-primary.test not ready: waiting for rollout to finish: observed deployment generation less than desired generation
0s          Normal    ScalingReplicaSet       deployment/podinfo-primary       Scaled up replica set podinfo-primary-5ccb749f7d to 1
0s          Normal    ScalingReplicaSet       deployment/podinfo-primary       Scaled up replica set podinfo-primary-5ccb749f7d to 1
0s          Normal    Injected                deployment/podinfo-primary       Linkerd sidecar proxy injected
0s          Normal    SuccessfulCreate        replicaset/podinfo-primary-5ccb749f7d   Created pod: podinfo-primary-5ccb749f7d-dwd6v
0s          Normal    Scheduled               pod/podinfo-primary-5ccb749f7d-dwd6v    Successfully assigned test/podinfo-primary-5ccb749f7d-dwd6v to k3d-k3s-default-agent-1
0s          Normal    Pulled                  pod/podinfo-primary-5ccb749f7d-dwd6v    Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
0s          Normal    Created                 pod/podinfo-primary-5ccb749f7d-dwd6v    Created container linkerd-init
0s          Normal    Started                 pod/podinfo-primary-5ccb749f7d-dwd6v    Started container linkerd-init
0s          Normal    Pulled                  pod/podinfo-primary-5ccb749f7d-dwd6v    Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
0s          Normal    Created                 pod/podinfo-primary-5ccb749f7d-dwd6v    Created container linkerd-proxy
0s          Normal    Started                 pod/podinfo-primary-5ccb749f7d-dwd6v    Started container linkerd-proxy
0s          Normal    IssuedLeafCertificate   serviceaccount/default                  issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:49 +0000 UTC: 2d91b9ae5ad11530c6ea34de4e71af4c8a2b43618258f7660c95bbeb92123328
0s          Normal    Pulling                 pod/podinfo-primary-5ccb749f7d-dwd6v    Pulling image "quay.io/stefanprodan/podinfo:1.7.0"
0s          Normal    Pulled                  pod/podinfo-primary-5ccb749f7d-dwd6v    Successfully pulled image "quay.io/stefanprodan/podinfo:1.7.0" in 2.776170594s
0s          Normal    Created                 pod/podinfo-primary-5ccb749f7d-dwd6v    Created container podinfod
0s          Normal    Started                 pod/podinfo-primary-5ccb749f7d-dwd6v    Started container podinfod
0s          Normal    Synced                  canary/podinfo                          all the metrics providers are available!
0s          Normal    ScalingReplicaSet       deployment/podinfo                      Scaled down replica set podinfo-7bfd46f477 to 0
0s          Warning   Synced                  canary/podinfo                          HTTPRoute .test update error: resource name may not be empty while reconciling
0s          Normal    SuccessfulDelete        replicaset/podinfo-7bfd46f477           Deleted pod: podinfo-7bfd46f477-twbm7
0s          Normal    Killing                 pod/podinfo-7bfd46f477-twbm7            Stopping container linkerd-proxy
0s          Normal    Killing                 pod/podinfo-7bfd46f477-twbm7            Stopping container podinfod
0s          Normal    Synced                  canary/podinfo                          all the metrics providers are available!
0s          Normal    Synced                  canary/podinfo                          Initialization done! podinfo.test

(.venv)

$ kubectl -n test get svc
NAME              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
frontend          ClusterIP   10.43.127.150   <none>        8080/TCP   82s
podinfo-canary    ClusterIP   10.43.238.46    <none>        9898/TCP   36s
podinfo-primary   ClusterIP   10.43.85.8      <none>        9898/TCP   36s
podinfo           ClusterIP   10.43.212.85    <none>        9898/TCP   82s
(.venv)

$ kubectl -n test set image deployment/podinfo \
  podinfod=quay.io/stefanprodan/podinfo:1.7.1
deployment.apps/podinfo image updated
(.venv) 

$ kubectl -n test get ev --watch
Warning: short name "ev" could also match lower priority resource events.events.k8s.io
LAST SEEN   TYPE      REASON                  OBJECT                                  MESSAGE
2m16s       Normal    ScalingReplicaSet       deployment/load                         Scaled up replica set load-7f97579865 to 1
2m16s       Normal    Injected                deployment/load                         Linkerd sidecar proxy injected
2m16s       Normal    ScalingReplicaSet       deployment/frontend                     Scaled up replica set frontend-6957977dc7 to 1
2m16s       Normal    SuccessfulCreate        replicaset/load-7f97579865              Created pod: load-7f97579865-kbm2h
2m15s       Normal    Scheduled               pod/load-7f97579865-kbm2h               Successfully assigned test/load-7f97579865-kbm2h to k3d-k3s-default-agent-1
2m16s       Normal    Injected                deployment/frontend                     Linkerd sidecar proxy injected
2m15s       Normal    SuccessfulCreate        replicaset/frontend-6957977dc7          Created pod: frontend-6957977dc7-m7czk
2m15s       Normal    Scheduled               pod/frontend-6957977dc7-m7czk           Successfully assigned test/frontend-6957977dc7-m7czk to k3d-k3s-default-server-0
2m15s       Normal    ScalingReplicaSet       deployment/podinfo                      Scaled up replica set podinfo-7bfd46f477 to 1
2m15s       Normal    Injected                deployment/podinfo                      Linkerd sidecar proxy injected
2m15s       Normal    SuccessfulCreate        replicaset/podinfo-7bfd46f477           Created pod: podinfo-7bfd46f477-twbm7
2m15s       Normal    Scheduled               pod/podinfo-7bfd46f477-twbm7            Successfully assigned test/podinfo-7bfd46f477-twbm7 to k3d-k3s-default-agent-0
2m15s       Normal    Pulled                  pod/load-7f97579865-kbm2h               Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
2m15s       Normal    Created                 pod/load-7f97579865-kbm2h               Created container linkerd-init
2m15s       Normal    Pulled                  pod/podinfo-7bfd46f477-twbm7            Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
2m15s       Normal    Started                 pod/load-7f97579865-kbm2h               Started container linkerd-init
2m15s       Normal    Created                 pod/podinfo-7bfd46f477-twbm7            Created container linkerd-init
2m15s       Normal    Started                 pod/podinfo-7bfd46f477-twbm7            Started container linkerd-init
2m14s       Normal    Pulled                  pod/podinfo-7bfd46f477-twbm7            Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
2m14s       Normal    Created                 pod/podinfo-7bfd46f477-twbm7            Created container linkerd-proxy
2m14s       Warning   FailedMount             pod/frontend-6957977dc7-m7czk           MountVolume.SetUp failed for volume "cfg" : failed to sync configmap cache: timed out waiting for the condition
2m14s       Normal    Started                 pod/podinfo-7bfd46f477-twbm7            Started container linkerd-proxy
2m14s       Normal    IssuedLeafCertificate   serviceaccount/default                  issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:02 +0000 UTC: dff1b169e1bc4dd55c68f72ea36acbb17838d04b7e5cb72fd0f98ce48035cce1
2m14s       Normal    Pulling                 pod/podinfo-7bfd46f477-twbm7            Pulling image "quay.io/stefanprodan/podinfo:1.7.0"
2m14s       Normal    Pulled                  pod/load-7f97579865-kbm2h               Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
2m14s       Normal    Created                 pod/load-7f97579865-kbm2h               Created container linkerd-proxy
2m14s       Normal    Started                 pod/load-7f97579865-kbm2h               Started container linkerd-proxy
2m13s       Normal    IssuedLeafCertificate   serviceaccount/default                  issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:03 +0000 UTC: b7239570dbabc4ecb62d046413c1e9e1f6259033a10ce473a29c0ec47ed2ce1e
2m13s       Normal    Pulled                  pod/load-7f97579865-kbm2h               Container image "buoyantio/slow_cooker:1.2.0" already present on machine
2m13s       Normal    Created                 pod/load-7f97579865-kbm2h               Created container slow-cooker
2m13s       Normal    Pulled                  pod/frontend-6957977dc7-m7czk           Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
2m13s       Normal    Started                 pod/load-7f97579865-kbm2h               Started container slow-cooker
2m13s       Normal    Created                 pod/frontend-6957977dc7-m7czk           Created container linkerd-init
2m13s       Normal    Started                 pod/frontend-6957977dc7-m7czk           Started container linkerd-init
2m12s       Normal    Pulled                  pod/frontend-6957977dc7-m7czk           Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
2m12s       Normal    Created                 pod/frontend-6957977dc7-m7czk           Created container linkerd-proxy
2m12s       Normal    Started                 pod/frontend-6957977dc7-m7czk           Started container linkerd-proxy
2m12s       Normal    IssuedLeafCertificate   serviceaccount/default                  issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:04 +0000 UTC: 3e1b0fb8e147e90660266ca953aea49f2e120ef98a854078a78bc130477060b1
2m12s       Normal    Pulling                 pod/frontend-6957977dc7-m7czk           Pulling image "nginx:alpine"
2m11s       Normal    Pulled                  pod/podinfo-7bfd46f477-twbm7            Successfully pulled image "quay.io/stefanprodan/podinfo:1.7.0" in 2.947361578s
2m11s       Normal    Created                 pod/podinfo-7bfd46f477-twbm7            Created container podinfod
2m11s       Normal    Started                 pod/podinfo-7bfd46f477-twbm7            Started container podinfod
2m8s        Normal    Pulled                  pod/frontend-6957977dc7-m7czk           Successfully pulled image "nginx:alpine" in 4.249071928s
2m8s        Normal    Created                 pod/frontend-6957977dc7-m7czk           Created container nginx
2m8s        Normal    Started                 pod/frontend-6957977dc7-m7czk           Started container nginx
89s         Warning   Synced                  canary/podinfo                          podinfo-primary.test not ready: waiting for rollout to finish: observed deployment generation less than desired generation
89s         Normal    ScalingReplicaSet       deployment/podinfo-primary              Scaled up replica set podinfo-primary-5ccb749f7d to 1
89s         Normal    Injected                deployment/podinfo-primary              Linkerd sidecar proxy injected
89s         Normal    SuccessfulCreate        replicaset/podinfo-primary-5ccb749f7d   Created pod: podinfo-primary-5ccb749f7d-dwd6v
88s         Normal    Scheduled               pod/podinfo-primary-5ccb749f7d-dwd6v    Successfully assigned test/podinfo-primary-5ccb749f7d-dwd6v to k3d-k3s-default-agent-1
88s         Normal    Pulled                  pod/podinfo-primary-5ccb749f7d-dwd6v    Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
88s         Normal    Created                 pod/podinfo-primary-5ccb749f7d-dwd6v    Created container linkerd-init
88s         Normal    Started                 pod/podinfo-primary-5ccb749f7d-dwd6v    Started container linkerd-init
88s         Normal    Pulled                  pod/podinfo-primary-5ccb749f7d-dwd6v    Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
88s         Normal    Created                 pod/podinfo-primary-5ccb749f7d-dwd6v    Created container linkerd-proxy
87s         Normal    Started                 pod/podinfo-primary-5ccb749f7d-dwd6v    Started container linkerd-proxy
87s         Normal    IssuedLeafCertificate   serviceaccount/default                  issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:16:49 +0000 UTC: 2d91b9ae5ad11530c6ea34de4e71af4c8a2b43618258f7660c95bbeb92123328
87s         Normal    Pulling                 pod/podinfo-primary-5ccb749f7d-dwd6v    Pulling image "quay.io/stefanprodan/podinfo:1.7.0"
85s         Normal    Pulled                  pod/podinfo-primary-5ccb749f7d-dwd6v    Successfully pulled image "quay.io/stefanprodan/podinfo:1.7.0" in 2.776170594s
85s         Normal    Created                 pod/podinfo-primary-5ccb749f7d-dwd6v    Created container podinfod
84s         Normal    Started                 pod/podinfo-primary-5ccb749f7d-dwd6v    Started container podinfod
79s         Normal    ScalingReplicaSet       deployment/podinfo                      Scaled down replica set podinfo-7bfd46f477 to 0
79s         Warning   Synced                  canary/podinfo                          HTTPRoute .test update error: resource name may not be empty while reconciling
79s         Normal    SuccessfulDelete        replicaset/podinfo-7bfd46f477           Deleted pod: podinfo-7bfd46f477-twbm7
79s         Normal    Killing                 pod/podinfo-7bfd46f477-twbm7            Stopping container linkerd-proxy
79s         Normal    Killing                 pod/podinfo-7bfd46f477-twbm7            Stopping container podinfod
69s         Normal    Synced                  canary/podinfo                          all the metrics providers are available!
69s         Normal    Synced                  canary/podinfo                          Initialization done! podinfo.test
0s          Normal    Synced                  canary/podinfo                          New revision detected! Scaling up podinfo.test
0s          Normal    ScalingReplicaSet       deployment/podinfo                      Scaled up replica set podinfo-69c49997fd to 1
0s          Normal    Injected                deployment/podinfo                      Linkerd sidecar proxy injected
0s          Normal    SuccessfulCreate        replicaset/podinfo-69c49997fd           Created pod: podinfo-69c49997fd-bl9r7
0s          Normal    Scheduled               pod/podinfo-69c49997fd-bl9r7            Successfully assigned test/podinfo-69c49997fd-bl9r7 to k3d-k3s-default-agent-0
0s          Normal    Pulled                  pod/podinfo-69c49997fd-bl9r7            Container image "cr.l5d.io/linkerd/proxy-init:v2.4.1" already present on machine
0s          Normal    Created                 pod/podinfo-69c49997fd-bl9r7            Created container linkerd-init
0s          Normal    Started                 pod/podinfo-69c49997fd-bl9r7            Started container linkerd-init
0s          Normal    Pulled                  pod/podinfo-69c49997fd-bl9r7            Container image "cr.l5d.io/linkerd/proxy:edge-24.8.2" already present on machine
0s          Normal    Created                 pod/podinfo-69c49997fd-bl9r7            Created container linkerd-proxy
0s          Normal    Started                 pod/podinfo-69c49997fd-bl9r7            Started container linkerd-proxy
0s          Normal    IssuedLeafCertificate   serviceaccount/default                  issued certificate for default.test.serviceaccount.identity.linkerd.cluster.local until 2024-08-13 16:18:19 +0000 UTC: f494af297046c4dbac9483c0f92c82bb259f86470f8ba7e47eb4ebe4cdc14932
0s          Normal    Pulling                 pod/podinfo-69c49997fd-bl9r7            Pulling image "quay.io/stefanprodan/podinfo:1.7.1"
0s          Normal    Pulled                  pod/podinfo-69c49997fd-bl9r7            Successfully pulled image "quay.io/stefanprodan/podinfo:1.7.1" in 5.106073171s
0s          Normal    Created                 pod/podinfo-69c49997fd-bl9r7            Created container podinfod
0s          Normal    Started                 pod/podinfo-69c49997fd-bl9r7            Started container podinfod
0s          Normal    Synced                  canary/podinfo                          Starting canary analysis for podinfo.test
0s          Normal    Synced                  canary/podinfo                          Advance podinfo.test canary weight 10
0s          Normal    Synced                  canary/podinfo                          Advance podinfo.test canary weight 20
0s          Normal    Synced                  canary/podinfo                          Advance podinfo.test canary weight 30

(.venv) 
$ kubectl -n test get httproute.gateway.networking.k8s.io podinfo -o yaml
apiVersion: gateway.networking.k8s.io/v1beta1
kind: HTTPRoute
metadata:
  annotations:
    helm.toolkit.fluxcd.io/driftDetection: disabled
    kustomize.toolkit.fluxcd.io/reconcile: disabled
  creationTimestamp: "2024-08-12T16:16:37Z"
  generation: 5
  name: podinfo
  namespace: test
  ownerReferences:
  - apiVersion: flagger.app/v1beta1
    blockOwnerDeletion: true
    controller: true
    kind: Canary
    name: podinfo
    uid: cc8b370f-c44e-4bb0-a267-189698ae063b
  resourceVersion: "131678"
  uid: 8e2f6de0-4f06-4ee9-9fe0-e51f78f863b5
spec:
  parentRefs:
  - group: core
    kind: Service
    name: podinfo
    namespace: test
    port: 9898
  rules:
  - backendRefs:
    - group: ""
      kind: Service
      name: podinfo-primary
      port: 9898
      weight: 60
    - group: ""
      kind: Service
      name: podinfo-canary
      port: 9898
      weight: 40
    matches:
    - path:
        type: PathPrefix
        value: /
status:
  parents:
  - conditions:
    - lastTransitionTime: "2024-08-12T16:16:37Z"
      message: ""
      reason: Accepted
      status: "True"
      type: Accepted
    - lastTransitionTime: "2024-08-12T16:16:37Z"
      message: ""
      reason: ResolvedRefs
      status: "True"
      type: ResolvedRefs
    controllerName: linkerd.io/policy-controller
    parentRef:
      group: core
      kind: Service
      name: podinfo
      namespace: test
      port: 9898
(.venv) 
$ kubectl delete -k github.com/fluxcd/flagger/kustomize/linkerd && \
  kubectl delete ns test
# Warning: 'bases' is deprecated. Please use 'resources' instead. Run 'kustomize edit fix' to update your Kustomization automatically.
# Warning: 'patchesJson6902' is deprecated. Please use 'patches' instead. Run 'kustomize edit fix' to update your Kustomization automatically.
# Warning: 'patchesStrategicMerge' is deprecated. Please use 'patches' instead. Run 'kustomize edit fix' to update your Kustomization automatically.
namespace "flagger-system" deleted
customresourcedefinition.apiextensions.k8s.io "alertproviders.flagger.app" deleted
customresourcedefinition.apiextensions.k8s.io "canaries.flagger.app" deleted
customresourcedefinition.apiextensions.k8s.io "metrictemplates.flagger.app" deleted
serviceaccount "flagger" deleted
clusterrole.rbac.authorization.k8s.io "flagger" deleted
clusterrolebinding.rbac.authorization.k8s.io "flagger" deleted
deployment.apps "flagger" deleted
authorizationpolicy.policy.linkerd.io "prometheus-admin-flagger" deleted
namespace "test" deleted
```