import unittest
import json

from app import app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.headers = {'Content-Type': 'application/json'}

    def test_normal_query(self):
        response = self.client.post(
            '/', headers=self.headers, data=json.dumps({'questions_num': 4})
        )
        self.assertEqual(response.status_code, 200)

    def test_float_ques_num(self):
        response = self.client.post(
            '/', headers=self.headers, data=json.dumps({'questions_num': 2.5})
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_key(self):
        response = self.client.post(
            '/', headers=self.headers, data=json.dumps({'questions_nums': 2})
        )
        self.assertEqual(response.status_code, 400)
