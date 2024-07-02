#!/usr/bin/env python3
"""_summary_
        """

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    pass
