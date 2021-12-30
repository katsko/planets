#!/usr/bin/env python
from flask import Flask
from apium.handlers.flask.handler import api_handler


app = Flask(__name__)
app.add_url_rule('/api/', view_func=api_handler, methods=['POST'])
app.run('localhost', 10800, debug=True)
