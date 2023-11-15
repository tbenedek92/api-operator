import kopf
import requests
# from kubernetes import config

# Initialize the Kubernetes client
# config.load_kube_config()

@kopf.on.create('my-platfom.com', 'v1', 'managed-apis')
@kopf.on.update('my-platfom.com', 'v1', 'managed-apis')
def create_update_handler(spec, name, namespace, logger, **kwargs):
    # Extract the endpoint and payload data from the spec
    endpoint = spec.get('endpoint')
    payload = spec.get('payload', {})
    path = f'{endpoint}/update'

    # Ensure the endpoint URL is provided
    if not endpoint:
        logger.error(f"Endpoint not defined for ManagedApi {name} in namespace {namespace}")
        return {'status': 'Error: Endpoint not defined'}

    # Call the API endpoint with the payload
    response = requests.post(path, json=payload)
    logger.info(f"API called for ManagedApi {name} in namespace {namespace}, response: {response.status_code}")

    return {'status': 'Processed create/update event'}

@kopf.on.delete('my-platfom.com', 'v1', 'managed-apis')
def delete_handler(spec, name, namespace, logger, **kwargs):
    # Call the delete API endpoint
    endpoint = spec.get('endpoint')
    path = f'{endpoint}/delete'

    response = requests.post(path)
    logger.info(f"Delete API called for {name} in namespace {namespace}, response: {response.status_code}")

    return {'status': 'Processed delete event'}
