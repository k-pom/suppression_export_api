"""
    This controls user related methods (ie, validate API Key)
"""
from flask_restful import Resource
from exporter.logic import mailgun
from exporter.models.user import User


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

        try:
            mailgun.list_domains(User(apiKey))
            return {"apiKey": apiKey, "valid": True}
        except:
            return {"apiKey": apiKey, "valid": False}
