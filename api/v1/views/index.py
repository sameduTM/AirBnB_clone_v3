#!/usr/bin/python3
"""index file for views"""
from api.v1.views import app_views
import json

@app_views.route('/status')
def status():
	status_obj = {"status": "OK"} 
	return json.dumps(status_obj, indent=2)
