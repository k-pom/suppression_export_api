"""
This is app configuration, separate from application.py to
allow for other parts of the application to grab app without
circular dependencies.
"""

import sys
import logging
import traceback
from flask import Flask, render_template
from flask_restful import Api
from exporter.helpers.common import use_generated_assests

logging.basicConfig(level=logging.INFO)

app = Flask(__name__,
            static_folder='static',
            static_url_path='/static')


@app.route('/docs')
def docs():
    return render_template('docs.html')


@app.route('/')
@use_generated_assests
def index(css, js):
    return render_template('index.html', css=css, js=js)


class Service(Api):
    def handle_error(self, e):

        t, val, trace = sys.exc_info()
        last = traceback.extract_tb(trace).pop()

        if type(e) == KeyError:
            return self.make_response({
                "error": "Key not found: {} at {}:{}".format(val, last[0], last[1])
            }, 500)

        try:
            return self.make_response({"error": str(e)}, e.code)
        except:
            return self.make_response({"error": str(e)}, 500)


api = Service(app)
