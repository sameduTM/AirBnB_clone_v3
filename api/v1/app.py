#!/usr/bin/python3
"""main app of API"""
from flask import Flask, current_app
from models import storage
from api.v1.views import app_views
import os
import json

app = Flask(__name__)
app.register_blueprint(app_views)

api_host = os.getenv("HBNB_API_HOST", default='0.0.0.0')
api_port = os.getenv("HBNB_API_PORT", default=5000)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """close storage"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """a handler for 404 errors that returns a
    JSON-formatted 404 status code response.
    """
    error_json = {"error": "Not found"}
    return current_app.response_class(json.dumps(error_json, indent=2),
                                      mimetype="application/json", status=404)


if __name__ == "__main__":
    app.run(host=api_host, port=api_port, threaded=True)
