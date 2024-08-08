# Commands used:


![alt text](image.png)

this shit was miserable to try to get it working. still no idea what black magic I did so it connected.
```console
$ kubectl get configmap loki-loki-stack -n loki-stack -o yaml
apiVersion: v1
data:
  loki-stack-datasource.yaml: |-
    apiVersion: 1
    datasources:
    - name: Loki
      type: loki
      access: proxy
      url: "http://loki:3100"
      version: 1
      isDefault: true
      jsonData:
        {}
kind: ConfigMap
metadata:
  annotations:
    meta.helm.sh/release-name: loki
    meta.helm.sh/release-namespace: loki-stack
  creationTimestamp: "2024-08-05T19:03:14Z"
  labels:
    app: loki-stack
    app.kubernetes.io/managed-by: Helm
    chart: loki-stack-2.10.2
    grafana_datasource: "1"
    heritage: Helm
    release: loki
  name: loki-loki-stack
  namespace: loki-stack
  resourceVersion: "34120"
  uid: 3946f146-faaf-426d-bc44-d29f9c8ae5e8
```

curling with to-do too long:
```console
$ curl -X POST "http://localhost:8081/todos" -H "Content-Type: application/json" -d '{"content":"This todo content is way too long and should trigger a validation error because it exceeds the character limit of 140 characters imposed by the backend"}'
{"detail":[{"type":"value_error","loc":["body","content"],"msg":"Value error, Todo content too long","input":"This todo content is way too long and should trigger a validation error because it exceeds the character limit of 140 characters imposed by the backend","ctx":{"error":{}}}]}(.venv) 
```

curling:
```console
$ curl -X POST "http://localhost:8081/todos" -H "Content-Type: application/json" -d '{"content":"Testing 1 2 3 kjeh kjeh"}'
{"content":"Testing 1 2 3 kjeh kjeh"}(.venv) 
```

checking logs:
```console
$ kubectl logs todo-app-dep-b8456c9c-kpndk -c todo-backend
2024-08-05 21:03:24,146 - uvicorn.error - INFO - Started server process [1]
2024-08-05 21:03:24,146 - uvicorn.error - INFO - Waiting for application startup.        
2024-08-05 21:03:24,146 - uvicorn.error - INFO - Application startup complete.
2024-08-05 21:03:24,202 - uvicorn.error - INFO - Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
2024-08-05 21:04:00,607 - uvicorn.access - INFO - 10.42.1.4:48432 - "GET /todos HTTP/1.1" 200
2024-08-05 21:04:11,376 - main - INFO - Created to-do: Testing
2024-08-05 21:04:11,377 - uvicorn.access - INFO - 10.42.1.4:60112 - "POST /todos HTTP/1.1" 200
2024-08-05 21:05:01,560 - main - WARNING - Attempted to create a to-do with content too long: This todo content is way too long and should trigger a validation error because it exceeds the character limit of 140 characters imposed by the backend
2024-08-05 21:05:01,561 - uvicorn.access - INFO - 10.42.1.4:55328 - "POST /todos HTTP/1.1" 422
2024-08-05 21:05:55,672 - main - INFO - Created to-do: Testing 1 2 3 kjeh kjeh
2024-08-05 21:05:55,673 - uvicorn.access - INFO - 10.42.1.4:36502 - "POST /todos HTTP/1.1" 200
```



