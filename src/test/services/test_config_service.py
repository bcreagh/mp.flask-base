from services.config_service import ConfigService


def test_get_port():
    port = ConfigService.get_port()
    assert port == 5000


def test_get_service_name():
    port = ConfigService.get_service_name()
    assert port == 'flask-base'
