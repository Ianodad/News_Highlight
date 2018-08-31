from flask import Flask

# get debuging from config.py
# from .config import DevConfig


def create_news(config_name):

    # Initializing application object using the flask constructor
    app = Flask(__name__)

    # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
