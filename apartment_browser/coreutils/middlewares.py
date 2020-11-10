"""
Defines middlewares used to alter global application behaviour.
"""
import json
from datetime import datetime
from bson import ObjectId

import sanic
from .exceptions import APIError


async def _rest_error_handler(_request, exception):
    return exception.to_response()


async def _jsonify_response(_request, response):
    # return original response if object is a response
    if isinstance(response, sanic.response.HTTPResponse):
        return response

    # if object is of unknown type, use custom api encoder
    return sanic.response.HTTPResponse(
        json.dumps(response, cls=_APIEncoder), content_type="application/json"
    )


class _APIEncoder(json.JSONEncoder):
    def _serialize_datetime(self, obj):
        return float(obj.strftime("%s")) * 1000

    def _serialize_objectid(self, obj):
        return str(obj)

    def _serialize_default(self, obj):
        return super().default(obj)

    def default(self, obj):
        return {
            datetime: self._serialize_datetime,
            ObjectId: self._serialize_objectid,
        }.get(type(obj), self._serialize_default)(obj)


def register_rest_handler(app):
    """
    Register middlewares that intercept API requests and serialize it as JSON.
    """
    app.error_handler.add(APIError, _rest_error_handler)
    app.middleware("response", _jsonify_response)
