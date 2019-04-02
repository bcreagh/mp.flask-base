from flask import Blueprint, Response
import json

import app
from services.action_service import ActionService
from services.config_service import ConfigService


blueprint = Blueprint(__name__, __name__)
app.add_blueprint_to_list(blueprint)

service_name = ConfigService.get_service_name()


@blueprint.route('/{}/actions'.format(service_name))
def list_routes():
    all_actions = ActionService.get_all_actions()
    result = json.dumps(all_actions)
    response = Response(result, mimetype='application/json')
    return response
