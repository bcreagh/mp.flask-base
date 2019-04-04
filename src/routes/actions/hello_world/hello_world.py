from flask import Blueprint, Response, request
import json

from mp.utilities.logger.logger import Logger
from mp.utilities.stopwatch import Stopwatch
from services.action_service import ActionService
from services.config_service import ConfigService
import services.json_service as json_service
from mp.domain.action_result import ActionResult
import app


service_name = ConfigService.get_service_name()
blueprint = Blueprint(__name__, __name__)
app.add_blueprint_to_list(blueprint)


@blueprint.route('/{}/hello-world'.format(service_name), methods=['GET', 'POST'])
def get_hello_world():
    if request.method == 'GET':
        return hello_world_get()
    if request.method == 'POST':
        return hello_world_post()


def hello_world_get():
    Logger.log('Handling the GET request')
    action = ActionService.get_action('hello-world')
    with open('src/routes/actions/hello_world/hello_world.md') as readme:
        action['readme']['data'] = readme.read()
    result = json.dumps(action)
    response = Response(result, mimetype='application/json')
    return response


def hello_world_post():
    result = ActionResult()
    stopwatch = Stopwatch()
    user_input = request.get_json()['input']

    Logger.log('Handling the POST request', result)
    stopwatch.start()
    result.input = user_input
    result.output = 'Hello {}'.format(user_input)
    performance = stopwatch.stop()
    result.performance = performance
    response = Response(json_service.to_json(result), mimetype='application/json')
    return response
