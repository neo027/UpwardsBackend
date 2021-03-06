from rest_framework import status


class ErrorMessage(Exception):

    def __init__(self, msg):
        self.value = msg

    def __str__(self):
        return repr(self.value)


class ResponseException(Exception):

    def __init__(self, meta, response, status):
        self.response = response
        self.status = status
        self.meta = meta
        super(Exception, self).__init__(
            meta + ". Status Code: " + str(status))


class NotAcceptableError(ResponseException):

    def __init__(self, param, param_value, response={}):
        meta = '%s : %s Not Found' % (str(param), str(param_value))
        super(NotAcceptableError, self).__init__(
            meta, response, status.HTTP_406_NOT_ACCEPTABLE)


class ConflictError(ResponseException):

    def __init__(self, param, param_value, response={}):
        meta = '%s : %s Already Exists in Database' % (
            str(param), str(param_value))
        super(ConflictError, self).__init__(
            meta, response, status.HTTP_409_CONFLICT)
