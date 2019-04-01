from services.action_service import ActionService


def test_convert_to_action_object():
    assert ActionService._actions is ActionService.get_all_actions()


