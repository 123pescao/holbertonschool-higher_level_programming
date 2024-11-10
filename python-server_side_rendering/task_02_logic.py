#!/usr/bin/python3
from flask import Flask, render_template
import os
import json

# Set up the Flask application
app = Flask(__name__)

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Define route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Define route for items page
@app.route('/items')
def items():
    # Read the data from items.json
    if os.path.exists('items.json'):
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    else:
        items_list = []

    return render_template('items.html', items=items_list)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5000)