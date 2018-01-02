# https://pypi.python.org/pypi/tmdbv3api

# Implement your function here.
# The function will get the event as the first parameter with query/body properties:
# The function should return a Dictionary
import os
import json
import urlparse

from truffleHog import truffleHog as th
# from box import Box


def hog(event, context):
    params = event.get("query", {})
    outcome = th.find_strings(params['git_url'])
    return _build_response(outcome)


def manual_hog(git_url):
    outcome = th.find_strings(git_url, printJson=True)
    print(outcome)


def _build_response(response, stringify=False):
    response = json.dumps(response) if stringify else response
    return {
        'statusCode': 200,
        'body': response,
        'headers': {"Content-Type": "application/json"}
    }


if __name__ == '__main__':
    manual_hog('https://github.com/seekrets/seekrets.git')
