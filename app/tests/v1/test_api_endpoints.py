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
        response = self.app.test_client().get('/api/v1/meetups')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
