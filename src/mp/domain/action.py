from mp.domain.readme import Readme
from mp.domain.request_details.request_details import RequestDetails


class Action:
    def __init__(self):
        self.name = ''
        self.description = ''
        self.route = ''
        self.instructions = ''
        self.readme = Readme()
        self.examples = []
        self.requestDetails = RequestDetails()
