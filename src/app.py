from flask import Flask

_blueprint_list = []
flask_app = Flask(__name__)


def add_blueprint_to_list(blueprint):
    _blueprint_list.append(blueprint)


def register_all_blueprints():
    for blueprint in _blueprint_list:
        flask_app.register_blueprint(blueprint)
