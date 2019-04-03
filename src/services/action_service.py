import json


class ActionService:

    _actions = []

    @staticmethod
    def _initialise():
        with open('actions.json') as actions_file:
            ActionService._actions = json.load(actions_file)

    @staticmethod
    def get_all_actions():
        return ActionService._actions

    @staticmethod
    def get_action(route):
        result = None
        for action in ActionService._actions:
            if action['route'] == route:
                result = action
        if result is not None:
            return result
        else:
            raise ValueError('An action could not be found for the route {}'.format(route))


ActionService._initialise()
