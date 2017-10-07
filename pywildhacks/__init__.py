from .request import Request
from .exception import InvalidRequestException

class WildhacksClient(object):
    def __init__(self, host="http://localhost:8080/public"):
        self.host = host
        self.request = Request(host)

    def send_request(self, method, url, params={}, valid_parameters=[], requires_key=False):
        valid_methods = ["get"]
        method = method.strip().lower()

        if method not in valid_methods:
            raise InvalidRequestException()

        if method == "get":
            return self.request.get(url)

    def get_users(self):
        return self.send_request(method="bleh", url="/users")

    def get_events(self):
        return self.send_request(method="GET", url="/events")
    
    def get_talks(self):
        return self.send_request(method="GET", url="/talks")

    def get_teams(self):
        return self.send_request(method="GET", url="/teams")