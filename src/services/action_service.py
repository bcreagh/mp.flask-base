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


ActionService._initialise()
