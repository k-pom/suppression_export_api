from flask_restful import Resource
from flask import abort


class ExportResource(Resource):

    def get(self, export_id):
        """
            Download a single export
            This route is the full export download, as a CSV.

            Note: This is NOT json.
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
            responses:
                401: {}
                404: {}
                200:
                    description: A csv of the export download
        """
        abort(501)
        return

    def delete(self, export_id):
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
            responses:
                404: {}
                401: {}
                200:
                    description: The export has been deleted
        """
        abort(501)
        return {"success": True}
