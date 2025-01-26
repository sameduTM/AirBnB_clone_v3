#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    place_id = "nop"

    """ PUT /api/v1/cities/<place_id>
    """
    r = requests.put("http://0.0.0.0:5000/api/v1/places/{}".format(place_id), data=json.dumps({ 'name': "NewName" }), headers={ 'Content-Type': "application/json" })
    print(r.status_code)