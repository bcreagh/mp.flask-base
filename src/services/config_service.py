import json


class ConfigService:
    _config = {}

    @staticmethod
    def _initialise():
        with open('config.json') as config_file:
            ConfigService._config = json.load(config_file)

    @staticmethod
    def get_port():
        port = ConfigService._config['port']
        return port

    @staticmethod
    def get_service_name():
        service_name = ConfigService._config['service-name']
        return service_name


ConfigService._initialise()