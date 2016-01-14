from flask import Flask, render_template
from flask_restful import Api
import logging
import os
import glob
import sys
import traceback

logging.basicConfig(level=logging.INFO)
STATIC_DIR = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'static', 'gen')

app = Flask(__name__,
            static_folder='static',
            static_url_path='/static')


@app.route('/docs')
def docs():
    return render_template('docs.html')


@app.route('/')
def index():
    css_files = glob.glob(os.path.join(STATIC_DIR, '*.css'))
    css = [os.path.split(item)[1] for item in css_files]
    js_files = glob.glob(os.path.join(STATIC_DIR, '*.js'))
    js = [os.path.split(item)[1] for item in js_files]
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
