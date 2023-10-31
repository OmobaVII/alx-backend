#!/usr/bin/env python3
""" This module instantiate Babel object in the app """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ a class that configures the app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('5-app.Config')


@app.route('/', strict_slashes=False)
def index() -> str:
    """ returns 5-index.html page """
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """ determines the best match for the user's languages """
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """ Returns the user dict if the ID is found """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
        else:
            return None


@app.before_request
def before_request():
    """ Finds a user and sets as the global on flask.g.user """
    g.user = get_user()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
