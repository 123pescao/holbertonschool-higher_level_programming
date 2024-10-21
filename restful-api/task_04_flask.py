#!/usr/bin/python3
"""Simple API using Flask"""
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    """Home route"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    """Returns a list of usernames"""
    return jsonify(list(users.keys())), 200

@app.route('/status')
def status():
    """Returns the status of the API"""
    return "OK", 200

@app.route('/users/<username>')
def get_user(username):
    """Returns user details for a given username"""
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user"""
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400

    data = request.get_json()
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run()
