from flask import Flask, redirect, render_template
from flask_restful import Api
import logging
import os

logging.basicConfig(level=logging.INFO)

app = Flask(__name__,
            static_folder='static',
            static_url_path='/static')


@app.route('/docs')
def index():
    return render_template('docs.html')


class Service(Api):
    def handle_error(self, e):
        return self.make_response({"error": str(e)}, 500)


api = Service(app)
