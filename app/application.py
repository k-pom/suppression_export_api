#! /usr/bin/env python

from exporter.http import export_list, export, docs, user
from app import api, app as application

resources = {
    '/exports': export_list.ExportListResource,
    '/exports/<int:export_id>': export.ExportResource,
    '/users/<string:apiKey>': user.ApiKeyResource,
    '/docs.json': docs.DocsResource
}

for route, resource in resources.items():
    api.add_resource(resource, route)

if __name__ == '__main__':
    application.run(debug=True, processes=3)
