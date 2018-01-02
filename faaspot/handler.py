import json

from truffleHog import truffleHog as th


def hog(event, context):
    params = event.get("query", {})
    outcome = th.find_strings(params['git_url'])
    return _build_response(outcome)


def _build_response(response, stringify=False):
    response = json.dumps(response) if stringify else response
    return {
        'statusCode': 200,
        'body': response,
        'headers': {"Content-Type": "application/json"}
    }
