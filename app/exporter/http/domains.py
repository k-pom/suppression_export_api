from flask_restful import Resource
from flask import abort, request
import requests


class DomainListResource(Resource):

    def get(self):
        """
            List domains
            This route lists all domains the user has access to see
            ---
            tags:
                - Export List
            responses:
                401: {}
                200:
                    description: A list of domains is returned
        """

        print("Headers: ")
        print(request.headers)
        token = request.headers.get('X-Auth-Token', None)
        if token is None:
            abort(401)

        url = "https://api.mailgun.net/v3/domains"

        response = requests.get(url, auth=('api', token))
        data = response.json()['items']
        from pprint import pprint
        pprint(data)
        return {"domains": data}
