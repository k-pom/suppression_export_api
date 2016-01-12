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
        abort(501)
        return {"exports": []}


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
                    description: An export will been created. An ID to reference it by will be returned as part of this
        """
        abort(501)
        return {"exports": []}
