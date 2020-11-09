"""
Declare custom exception used in apartment_browser package.
"""
import sanic


class ApartmentBrowserException(Exception):
    """
    Base exception for all exceptions defined here.
    """
    pass


class APIError(ApartmentBrowserException):
    """
    Special exception that can be serialized in API.
    """

    def __init__(self, message, status=500, **info):
        super().__init__(message)
        self._json = dict(message=message, **info)
        self._status = status

    def to_response(self):
        """
        Convert this exception into sanic response to be returned by API.
        """
        return sanic.response.json(
            self._json, status=self._status
        )
