from flask import Flask
from .routes import base


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(base.bp)

    app.config.from_pyfile("config.py")

    return app
