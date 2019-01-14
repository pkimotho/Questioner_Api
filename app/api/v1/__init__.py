from flask import Blueprint
from flask_restful import Resource, Api

# Local imports
from app.api.v1.views.meetup_view import MeetUps, MeetUpItem

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(version_one)

api.add_resource(MeetUps, '/meetups')
api.add_resource(MeetUpItem, '/meetups/<int:id>')
