import kopf
import kubernetes
import requests
from kubernetes.client.rest import ApiException

@kopf.on.create('example.com', 'v1', 'dummysites')
def create_dummysite(body, spec, **kwargs):
    name = body['metadata']['name']
    namespace = body['metadata']['namespace']
    website_url = spec['website_url']

    try:
        content = requests.get(website_url).text
    except requests.RequestException as e:
        raise kopf.PermanentError(f"Failed to fetch website content: {e}")

    config_map = {
        'apiVersion': 'v1',
        'kind': 'ConfigMap',
        'metadata': {
            'name': f"{name}-content",
            'namespace': namespace
        },
        'data': {
            'index.html': content
        }
    }

    api = kubernetes.client.CoreV1Api()
    try:
        api.create_namespaced_config_map(namespace, config_map)
    except ApiException as e:
        raise kopf.PermanentError(f"Failed to create ConfigMap: {e}")

    pod = {
        'apiVersion': 'v1',
        'kind': 'Pod',
        'metadata': {
            'name': f"{name}-pod",
            'namespace': namespace
        },
        'spec': {
            'containers': [{
                'name': 'nginx',
                'image': 'nginx:alpine',
                'ports': [{'containerPort': 80}],
                'volumeMounts': [{
                    'name': 'content',
                    'mountPath': '/usr/share/nginx/html'
                }]
            }],
            'volumes': [{
                'name': 'content',
                'configMap': {
                    'name': f"{name}-content"
                }
            }]
        }
    }

    try:
        api.create_namespaced_pod(namespace, pod)
    except ApiException as e:
        raise kopf.PermanentError(f"Failed to create Pod: {e}")

    service = {
        'apiVersion': 'v1',
        'kind': 'Service',
        'metadata': {
            'name': f"{name}-service",
            'namespace': namespace
        },
        'spec': {
            'selector': {'app': f"{name}-pod"},
            'ports': [{'port': 80, 'targetPort': 80}]
        }
    }

    try:
        api.create_namespaced_service(namespace, service)
    except ApiException as e:
        raise kopf.PermanentError(f"Failed to create Service: {e}")

    return {'message': 'DummySite resources created successfully'}