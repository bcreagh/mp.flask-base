from flask import Blueprint, Response
import json

import app
from services.config_service import ConfigService


blueprint = Blueprint(__name__, __name__)
app.add_blueprint_to_list(blueprint)

service_name = ConfigService.get_service_name()


@blueprint.route('/{}/readme'.format(service_name))
def list_routes():
    readme = {}
    with open('README.md') as readme_file:
        readme['data'] = readme_file.read()
    response = Response(json.dumps(readme), mimetype='application/json')
    return response
