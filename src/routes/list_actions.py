from flask import Blueprint, Response
import json


import app
from services.action_service import ActionService


blueprint = Blueprint(__name__, __name__)
app.add_blueprint_to_list(blueprint)


@blueprint.route('/flask-base/actions')
def list_routes():
    all_actions = ActionService.get_all_actions()
    result = json.dumps(all_actions)
    response = Response(result, mimetype='application/json')
    return response



