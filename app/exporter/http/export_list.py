from flask_restful import Resource
from flask import abort


class ExportListResource(Resource):

    def get(self):
        """
            List exports
            This route lists all exports the user has access to see
            ---
            tags:
                - Export List
            responses:
                401: {}
                200:
                    description: A list of exports is returned
        """
        return {"exports": [1,2,3]}

    def post(self):
        """
            Create a new export
            This route creates a fires of a call to create a new export.
            ---
            tags:
                - Export List
            responses:
                400: {}
                401: {}
                200:
                    description: An export will been created
        """
        abort(501)
        return {"exports": []}
