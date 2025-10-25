#!/usr/bin/env python3
"""
Flask app to serve the site with Bootstrap-based templates and a tiny API.
Routes: /, /about, /projects, /contact, /api/hello
"""
from flask import Flask, render_template, jsonify
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# templates are in <workspace>/templates
app = Flask(__name__, static_folder=STATIC_DIR, template_folder=os.path.join(BASE_DIR, 'templates'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/api/hello')
def api_hello():
    return jsonify({
        'message': 'Hello from Flask backend',
        'status': 'ok'
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
