#!/usr/bin/python3
"""view for State objects that handles all default RESTFul API actions"""
from api.v1.views import app_views
from flask import Flask, current_app, abort
from flask import jsonify
from flask import make_response
from flask import json
from flask import request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def getStates():
    """retrieve the list of all State objects"""
    all_states = storage.all(State)
    obj_list = []
    for key, value in all_states.items():
        obj_list.append(value.to_dict())
    return make_response(jsonify(obj_list))


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def getState(state_id):
    """retrieve a state object"""
    all_states = storage.all(State)
    for key, val in all_states.items():
        obj_id = key.split('.')[1]
        if obj_id == state_id:
            val = val.to_dict()
            return make_response(jsonify(val))
    abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete(state_id):
    """deletes a state object"""
    all_states = storage.all(State)
    for key, val in all_states.items():
        obj_id = key.split('.')[1]
        if obj_id == state_id:
            storage.delete(val)
            storage.save()
            return make_response(jsonify({}), 200)
    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def createState():
    """create a State"""
    new_state = State()
    try:
        data = request.get_json()
    except Exception as e:
        return make_response("Not a JSON", 400)
    if not "name" in data:
        return make_response("Missing name", 400)
    for key, value in data.items():
        setattr(new_state, key, value)
    storage.new(new_state)
    storage.save()
    return make_response(jsonify(new_state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update(state_id):
    """update a state object"""
    all_states = storage.all(State)
    try:
        data = request.get_json()
    except Exception as e:
        return make_response("Not a JSON", 400)
    for key, value in all_states.items():
        obj_id = key.split('.')[1]
        if obj_id == state_id:
            value.name = data["name"]
            storage.save()
            return make_response(jsonify(value.to_dict()), 200)
    abort(404)
