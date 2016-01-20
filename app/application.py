#! /usr/bin/env python
"""
    This is the initial entry point for the application
"""

import os
from app import api, app as application
from exporter.http import export_list, export, docs, user, domains

resources = {
    '/domains/<string:domain>/exports': export_list.ExportListResource,
    '/exports/<string:export_id>': export.ExportResource,
    '/users/<string:api_key>': user.ApiKeyResource,
    '/domains': domains.DomainListResource,
    '/docs.json': docs.DocsResource
}

for route, resource in resources.items():
    api.add_resource(resource, route)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=os.environ.get('PORT', 5000), processes=3, debug=True)
