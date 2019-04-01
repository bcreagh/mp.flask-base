import json


class ActionService:

    _actions = []

    @staticmethod
    def _initialise():
        with open('actions.json') as actions_file:
            ActionService._actions = json.load(actions_file)
            print('here are the actions....')
            print(ActionService._actions)

    @staticmethod
    def get_all_actions():
        print('aboutt o be gotten')
        return ActionService._actions


ActionService._initialise()
