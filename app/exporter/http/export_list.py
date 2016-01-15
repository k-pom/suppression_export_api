from flask_restful import Resource
from flask import request
from exporter.helpers.auth import require_user
from exporter.logic import exports


class ExportListResource(Resource):

    @require_user
    def get(self, user, domain):
        """
            List exports
            This route lists all exports the user has access to see
            ---
            tags:
                - Export
            parameters:
                -
                    in: path
                    name: domain
                    description: Domain name to list exports for
                    type: string
                    required: true
                -
                    in: header
                    name: X-Auth-Token
                    description: Mailgun token
                    type: string
                    required: true
            responses:
                401: {}
                200:
                    description: A list of exports is returned
        """

        export_list = [e.serialize() for e in exports.list(user, domain)]
        return {
            "total": len(export_list),
            "exports": export_list
        }

    @require_user
    def post(self, user, domain):
        """
            Create a new export
            This route creates a fires of a call to create a new export.
            ---
            tags:
                - Export
            parameters:
                -
                    in: path
                    name: domain
                    description: Domain name to create export for
                    type: string
                    required: true
                -
                    in: header
                    name: X-Auth-Token
                    description: Mailgun token
                    type: string
                    required: true
                -
                    in: body
                    name: body
                    schema:
                        id: newExport
                        properties:
                            type:
                                type: string
                                required: true
                                description: bounce, complaint, unsubscribed
            responses:
                400: {}
                401: {}
                200:
                    description: An export will be created
        """
        data = request.get_json(force=True)

        new_export = exports.create(user, domain, data['type'])
        return {"export": new_export.serialize()}
