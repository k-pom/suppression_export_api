"""
    This contains methods for single export (delete)
"""
from exporter.helpers.auth import require_user
from exporter.logic import exports
from flask_restful import Resource


class ExportResource(Resource):

    @require_user
    def delete(self, api_key, export_id):
        """
            Delete an export.
            Delete the given export, both from the database, and from the
            filesystem.
            ---
            tags:
                - Export
            parameters:
                -
                    in: path
                    name: export_id
                    description: Export Id
                    type: int
                    required: true
                -
                    in: header
                    name: X-Auth-Token
                    description: Mailgun token
                    type: string
                    required: true
            responses:
                404: {}
                401: {}
                200:
                    description: The export has been deleted
        """
        exports.delete(api_key, export_id)
        return {"success": True}
