#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

# Config class to define available languages and set default locale and timezone
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)


# get_locale function to determine the best match for supported languages
@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template(
        '4-index.html',
        home_title=_("Welcome to Holberton"),
        home_header=_("Hello world!")
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

