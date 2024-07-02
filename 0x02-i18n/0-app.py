#!/usr/bin/env python3
"""_summary_
        """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    pass


if __name__ == '__main__':
    app.run()
