from flask import jsonify, request, make_response
from flask_restful import Resource
import datetime

# Local imports
from app.api.v1.models.meetup_model import meetUps, meetup


class MeetUps(Resource):
    def __init__(self):
        self.db = meetUps()

    def post(self):
        data = request.get_json()
        topic = data['topic']
        location = data['location']
        name = data['name']
        happeningOn = data['happeningOn']

        resp = self.db.save(location, topic, name, happeningOn)
        status = 201

        return make_response(jsonify({
            'status': status,
            "These are the Meetups": resp
        }), 201)

    def get(self):
        status = 200
        resp = self.db.get_meetUps()
        return make_response(jsonify({
            "status": status,
            "My Meetups": resp
        }), 200)
