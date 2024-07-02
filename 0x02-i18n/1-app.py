#!/usr/bin/env python3
"""_summary_
        """

from flask import Flask
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]


@app.route('/')
def index():
    pass
