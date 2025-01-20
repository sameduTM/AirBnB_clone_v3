#!/usr/bin/python3
"""main app of API"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)

api_host = os.getenv("HBNB_API_HOST", default='0.0.0.0')
api_port = os.getenv("HBNB_API_PORT", default=5000)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """close storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host=api_host, port=api_port, threaded=True)
