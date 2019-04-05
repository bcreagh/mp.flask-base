from flask import Response
import services.json_service as json_service


def handle_options():
    options = {'Allow': 'POST'}, 200, {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'PUT,GET'}
    response = Response(json_service.to_json(options), mimetype='application/json')
    return response
