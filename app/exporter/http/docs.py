from app import app
from flask_swagger import swagger
from flask_restful import Resource
from flask import jsonify


class DocsResource(Resource):
    def get(self):

        swag = swagger(app)
        swag['info']['version'] = "2.0"
        swag['info']['title'] = "Suppression Export API"

        for path, methods in swag['paths'].items():
            for method, info in methods.items():
                if "401" in info['responses'].keys():
                    info['responses']["401"] = {
                        "description": "User is not authenticated"
                    }
                if "400" in info['responses'].keys():
                    info['responses']["401"] = {
                        "description": "Request body was malformed"
                    }
                if "404" in info['responses'].keys():
                    info['responses']["404"] = {
                        "description": "Resource could not be found"
                    }

        return jsonify(swag)
