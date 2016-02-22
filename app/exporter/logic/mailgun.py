"""
    This module is responsible for all mailgun API calls.
"""

import requests

endpoint = "https://api.mailgun.net/v3"


def _get(url, api_key):
    return requests.get(url, auth=('api', api_key))


def list_domains(api_key):
    url = "{}/domains".format(endpoint)
    response = _get(url, api_key)
    response.raise_for_status()
    return response.json()['items']


def list_suppressions(export, url=None):
    if url is None:
        url = "{}/{}/{}".format(endpoint, export.domain, export.type)
    return _get(url, export.user).json()
