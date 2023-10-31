#!/usr/bin/env python3
""" This module instantiate Babel object in the app """
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config:
    """ a class that configures the app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """ returns 0-index.html page """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """ determines the best match for the user's
    preferred languages """
    return request.accept_languages.best_match(app.config.languages)


if __name__ == "__main__":
    app.run()
