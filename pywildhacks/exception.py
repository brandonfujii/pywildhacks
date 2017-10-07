class ApiException(Exception):
    def __init__(self, name=None, message=None):
        self.name = "Api exception" if name is None else name
        self.message = "Something went wrong!" if message is None else message

    def __str__(self):
        return "[%s]: %s" % (self.name, self.message)

class InvalidRequestException(ApiException):
    def __init__(self, name=None, message=None):
        self.name = "Invalid Request Exception"
        self.message = "Invalid request method or body"
    
