from mp.utilities.logger.log import Log


class Logger:

    @staticmethod
    def log(message, result=None):
        print(message)
        if result is not None:
            log = Log('log', message)
            result.logs.append(log)

    @staticmethod
    def error(message, result=None):
        print(message)
        if result is not None:
            log = Log('log', message)
            result.logs.append(log)
