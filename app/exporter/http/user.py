"""
    This controls user related methods (ie, validate API Key)
"""
from flask_restful import Resource
from exporter.logic import mailgun


class ApiKeyResource(Resource):

    def get(self, api_key):
        """
            Validate an API Key
            Calling mailgun, validate the API key
            ---
            tags:
                - User
            parameters:
                -
                    in: path
                    name: api_key
                    description: API Key
                    type: string
                    required: true
            responses:
                200:
                    description: The token is valid
        """

        try:
            mailgun.list_domains(api_key)
            return {"api_key": api_key, "valid": True}
        except:
            return {"api_key": api_key, "valid": False}
