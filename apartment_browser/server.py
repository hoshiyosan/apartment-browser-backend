"""
Instanciate sanic asgi app to expose an API,
and register middleware and endpoints.
"""
import sanic
from .coreutils.middlewares import register_rest_handler
from .routes import register_routes

asgi_app = sanic.Sanic()

# register middlewares
register_rest_handler(asgi_app)

# register routes in current app
register_routes(asgi_app)
