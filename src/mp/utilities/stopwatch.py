import datetime


class Stopwatch:

    def __init__(self):
        self.stopwatch_has_started = False
        self.start_time = 0

    def start(self):
        if self.stopwatch_has_started:
            raise Exception('The stopwatch has already been started')
        self.stopwatch_has_started = True
        self.start_time = Stopwatch.get_current_time()

    def stop(self):
        if not self.stopwatch_has_started:
            raise Exception('You cannot stop the stopwatch if it has not yet been started!')
        current_time = Stopwatch.get_current_time()
        time_elapled = (current_time - self.start_time).total_seconds() * 1000000
        self.stopwatch_has_started = False
        return time_elapled

    @staticmethod
    def get_current_time():
        return datetime.datetime.now()
