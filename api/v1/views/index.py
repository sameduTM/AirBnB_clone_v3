#!/usr/bin/python3
"""index file for views"""
from api.v1.views import app_views
from flask import jsonify, json, current_app

@app_views.route('/status')
def status():
	o_dct = {"status": "OK"}

	return current_app.response_class(json.dumps(o_dct, indent=2),
		mimetype="application/json")