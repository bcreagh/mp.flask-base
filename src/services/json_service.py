from datetime import time, date
import json


def to_json(obj):
    return json.dumps(obj, default=serialize)


# https://stackoverflow.com/questions/10252010/serializing-class-instance-to-json
def serialize(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    if isinstance(obj, time):
        serial = obj.isoformat()
        return serial

    return obj.__dict__
