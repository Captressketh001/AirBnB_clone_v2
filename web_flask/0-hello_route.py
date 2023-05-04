#!/usr/bin/python3
"""a script that starts a Flask web application"""
from web_flask import app

@app.route("/", strict_slashes=False)
def index():
    """Return HBNB when routed to /"""
    return "Hello HBNB"