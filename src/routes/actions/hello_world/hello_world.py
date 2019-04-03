from flask import Blueprint, Response
import json

from mp.utilities.logger.logger import Logger
from mp.utilities.stopwatch import Stopwatch
from services.action_service import ActionService
from services.config_service import ConfigService
from mp.domain.action_result import ActionResult
import app


service_name = ConfigService.get_service_name()
blueprint = Blueprint(__name__, __name__)
app.add_blueprint_to_list(blueprint)


@blueprint.route('/{}/hello-world'.format(service_name))
def get_hello_world():
    Logger.log('Handling the GET request')
    action = ActionService.get_action('hello-world')
    with open('src/routes/actions/hello_world/hello_world.md') as readme:
        action['readme']['data'] = readme.read()
    result = json.dumps(action)
    response = Response(result, mimetype='application/json')
    return response
