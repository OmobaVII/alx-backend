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


app.config.from_object('4-app.Config')


@app.route('/', strict_slashes=False)
def index() -> str:
    """ returns 0-index.html page """
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """ determines the best match for the user's languages """
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
