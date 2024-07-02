#!/usr/bin/env python3
"""_summary_
        """

from flask import Flask, render_template

app = Flask(__name__)


def index():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
