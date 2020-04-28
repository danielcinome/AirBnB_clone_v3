#!/usr/bin/python3
""" Status of your API """
from flask import Flask, render_template
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


print('This is a app_views {} -------'.format(app_views))

@app.teardown_appcontext
def teardown_app_context(self):
    storage.close()

if __name__ == '__main__':
    host = '0.0.0.0'
    port = '5000'
    if getenv('HBNB_API_HOST'):
        host = getenv('HBNB_API_HOST')
    if getenv('HBNB_API_PORT'):
        port = getenv('HBNB_API_PORT')
    app.run(host=host, port=port, threaded=True)
