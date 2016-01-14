from exporter.models.user import User
from functools import wraps
from flask import request


def require_user(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        kwargs['user'] = User(request.headers.get('X-Auth-Token', None))
        # TODO: Validate they are a real user
        return f(*args, **kwargs)

    return wrapper
