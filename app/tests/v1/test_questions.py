import os
import json
import unittest
from app import create_app


class TestApiEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

    def test_getquestions(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        resp = self.app.test_client().get('/api/v1/questions')
        self.assertEqual(resp.status_code, 200)

    """def test_postmeetups(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        resp = self.app.test_client().post('api/v1/meetups', data=json.dumps({
            "name": "Koof",
            "topic": "Python Enthusiasts Meetup",
            "location": "Nairobi",
            "happeningOn": "2019-05-23"
        }), headers={'content_type': 'application/json'})
        self.assertEqual(resp.status_code, 201)"""


if __name__ == '__main__':
    unittest.main()
