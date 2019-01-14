from flask import jsonify, request, make_response
from flask_restful import Resource
import datetime

# Local imports
from app.api.v1.models.question_model import questions, question


class Questions(Resource):
    def __init__(self):
        self.db = questions()

    def post(self):
        data = request.get_json()
        title = data['title']
        meetup = data['meetup']
        name = data['name']
        body = data['body']
        votes = data['votes']

        resp = self.db.save(title, meetup, name, body, votes)
        status = 201

        return make_response(jsonify({
            'status': status,
            "These are the Questions": resp
        }), 201)

    def get(self):
        status = 200
        resp = self.db.get_questions()
        return make_response(jsonify({
            "status": status,
            "All Questions": resp
        }), 200)
