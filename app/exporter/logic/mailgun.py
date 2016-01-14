import requests

endpoint = "https://api.mailgun.net/v3"


def list_domains(user):

    url = "{}/domains".format(endpoint)
    response = requests.get(url, auth=('api', user.key))
    return response.json()['items']
