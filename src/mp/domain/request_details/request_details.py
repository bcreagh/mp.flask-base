import mp.domain.request_details.http_methods as http_methods
import mp.domain.request_details.input_types as input_types


class RequestDetails:
    def __init__(self):
        self.httpMethod = http_methods.POST
        self.inputType = input_types.JSON
        self.inputTemplate = ''
