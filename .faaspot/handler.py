import json

from truffleHog import truffleHog as th


def hog(event, context):
    params = event.get("query", {})
    outcome = th.find_strings(params['git_url'])
    return _build_response(outcome)


def _build_response(response, stringify=False):
    response = json.dumps(response) if stringify else response
    print({
        'statusCode': 200,
        'body': response,
        'headers': {"Content-Type": "application/json"}
    })
    return {
        'statusCode': 200,
        'body': response,
        'headers': {"Content-Type": "application/json"}
    }


if __name__ == '__main__':
    event_stub = {
        'query': {'git_url': 'https://github.com/seekrets/seekrets.git'}}
    hog(event_stub, '')
