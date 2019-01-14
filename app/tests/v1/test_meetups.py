import os
import json
import unittest
from app import create_app


class TestApiEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

    def test_getmeetups(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        resp = self.app.test_client().get('/api/v1/meetups')
        self.assertEqual(resp.status_code, 200)

    """def test_postmeetups(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        resp = self.client().post('api/v1/meetups', data=json.dumps(dict(
            name="Koof"
        )), headers={'content_type': 'application/json'})
        self.assertEqual(resp.status_code, 201)"""

    def test_getmeetupsbyid(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        response = self.client().post('/api/v1/meetups/<int:meetupId>', data=json.dumps({

            "name": "Koof",
            "location": "Nairobi",
            "topic": "Python",
            "happeningOn": "2019-05-23"

        }), headers={'content-type': 'application/json'})
        item = self.client().get('api/v1/meetups/1')

        self.assertEqual(item.status_code, 200)


if __name__ == '__main__':
    unittest.main()
