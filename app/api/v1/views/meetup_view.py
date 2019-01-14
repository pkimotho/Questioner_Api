from flask import jsonify, request, make_response
from flask_restful import Resource
import datetime
import json

# Local imports
from app.api.v1.models.meetup_model import meetUps, meetup


class MeetUps(Resource):
    def __init__(self):
        self.db = meetup
        self.items = meetUps()

    def post(self):
        data = request.get_json()

        resp = self.items.save(
            data["name"], data["location"], data["topic"], data["happeningOn"])
        status = 201

        return make_response(jsonify({
            'status': status,
            "Message": "Meetup Created"
        }), 201)

    def get(self):
        status = 200
        resp = self.items.get_meetUps()
        if not resp:
            return {
                "Status": 400,
                "Message": "There are no meetups for now"
            }
        return make_response(jsonify({
            "status": status,
            "My Meetups": resp
        }), 200)


class MeetUpItem(Resource):
    def __init__(self):
        self.db = meetup
        self.items = meetUps()

    def get(self, id):
        status = 200
        resp = self.items.get_meetUpsById(id)
        if not resp:
            return {
                "Status": 400,
                "Message": "Meetup does not exist"
            }
        return make_response(jsonify({
            "status": status,
            "Meetup": resp
        }))
