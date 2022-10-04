from aula0 import app

import unittest


class TestApp(unittest.TestCase):

    def setUp(self):
        application = app.test_client()
        self.response = application.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_html_string_response(self):
        self.assertEqual({"message": "Hello World!"}, self.response.json)

    def test_content_type(self):
        self.assertIn('application/json', self.response.content_type)

    def test_api_route(self):
        application = app.test_client()
        getresponse = application.get('/api')
        self.assertEqual({"message": "Hello API!",
                         "method": "GET", "status": 200}, getresponse.json)
        self.assertEqual(200, getresponse.status_code)

    def test_post_api_route(self):
        application = app.test_client()
        postresponse = application.post('/api')
        self.assertEqual(None, postresponse.json)
        self.assertEqual(400, postresponse.status_code)

    def test_post_person_api(self, person="123", name="John"):
        application = app.test_client()
        postresponse = application.post('/api/'+person + '?name='+name)
        self.assertEqual(
            {"user_code": person, "name": "John"}, postresponse.json)
        self.assertEqual(200, postresponse.status_code)

    def test_post_person_api_without_name(self, person="123"):
        application = app.test_client()
        postresponse = application.post('/api/'+person)
        self.assertEqual(
            {"user_code": person, "name": None}, postresponse.json)
        self.assertEqual(200, postresponse.status_code)

    def test_post_person_api_without_person(self):
        application = app.test_client()
        postresponse = application.post('/api/')
        self.assertEqual(404, postresponse.status_code)

    def test_post_json_data_to_api(self):
        application = app.test_client()
        postresponse = application.post('/api', json={"name": "John"})
        self.assertEqual(200, postresponse.status_code)
        self.assertEqual({"message": "POST", "data": {
                         "name": "John"}}, postresponse.json)
