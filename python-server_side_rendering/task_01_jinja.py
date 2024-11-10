#!/usr/bin/python3
from flask import Flask, render_template

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

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
