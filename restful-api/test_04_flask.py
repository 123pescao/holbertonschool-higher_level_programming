import unittest
import json
from task_04_flask import app, users


class FlaskAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        users.clear()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Welcome to the Flask API!')

    def test_status_route(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'OK')

    def test_add_user(self):
        # Add a user
        user_data = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        response = self.app.post('/add_user', data=json.dumps(user_data), content_type='application/json')
        print("Response Status Code (add_user):", response.status_code)  # Debug statement
        print("Response Data (add_user):", response.data.decode())  # Debug statement
        self.assertEqual(response.status_code, 201)
        self.assertIn("User added", response.data.decode())

    def test_add_duplicate_user(self):
        user_data = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        self.app.post('/add_user', data=json.dumps(user_data), content_type='application/json')

        response = self.app.post('/add_user', data=json.dumps(user_data), content_type='application/json')
        print("Response Status Code (add_duplicate_user):", response.status_code)  # Debug statement
        print("Response Data (add_duplicate_user):", response.data.decode())  # Debug statement
        self.assertEqual(response.status_code, 400)
        self.assertIn("User already exists", response.data.decode())

    def test_get_usernames(self):
        users['john'] = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        response = self.app.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertIn("john", response.data.decode())

    def test_get_user(self):
        users['john'] = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        response = self.app.get('/users/john')
        self.assertEqual(response.status_code, 200)
        self.assertIn("John", response.data.decode())

    def test_user_not_found(self):
        response = self.app.get('/users/nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertIn("User not found", response.data.decode())

if __name__ == '__main__':
    unittest.main()
