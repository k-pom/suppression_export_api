from flask_restful import Resource
from flask import abort


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
        return {"domains": [1,2,3]}
