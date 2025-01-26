#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    
    place_id = "nop"
    
    """ Get user
    """
    r = requests.get("http://0.0.0.0:5000/api/v1/users")
    r_j = r.json()
    user_id = r_j[0].get('id')

    
    """ POST /api/v1/places/<place_id>/reviews
    """
    r = requests.post("http://0.0.0.0:5000/api/v1/places/{}/reviews/".format(place_id), data=json.dumps({ 'user_id': user_id, 'text': "NewReview" }), headers={ 'Content-Type': "application/json" })
    print(r.status_code)
    