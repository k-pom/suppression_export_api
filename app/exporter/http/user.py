from flask_restful import Resource
import requests


class ApiKeyResource(Resource):

    def get(self, apiKey):
        """
            Validate an API Key
            Calling mailgun, validate the API key
            ---
            tags:
                - User
            parameters:
                -
                    in: path
                    name: apiKey
                    description: API Key
                    type: string
                    required: true
            responses:
                200:
                    description: The token is valid
        """

        url = "https://api.mailgun.net/v3/domains"

        response = requests.get(url, auth=('api', apiKey))
        return {"apiKey": apiKey, "valid": response.status_code <=299}
