"""
    All routes related to mailgun domains
"""
from exporter.helpers.auth import require_user
from exporter.logic import mailgun
from flask_restful import Resource


class DomainListResource(Resource):

    @require_user
    def get(self, user):
        """
            List domains
            This route lists all domains the user has access to see
            ---
            tags:
                - Domains
            parameters:
                -
                    in: header
                    name: X-Auth-Token
                    description: Mailgun token
                    type: string
                    required: true
            responses:
                401: {}
                200:
                    description: A list of domains is returned
        """

        domains = mailgun.list_domains(user)
        return {"domains": domains, "total": len(domains)}
