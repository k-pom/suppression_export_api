import requests

endpoint = "https://api.mailgun.net/v3"


def _get(url, user_key):
    return requests.get(url, auth=('api', user_key))


def list_domains(user):
    url = "{}/domains".format(endpoint)
    response = _get(url, user.key)
    response.raise_for_status()
    return response.json()['items']


def list_suppressions(export, url=None):
    if url is None:
        url = "{}/{}/{}".format(endpoint, export.domain, export.type)
    return _get(url, export.user).json()
