"""
Auth related helper methods
"""
from exporter.models.user import User
from flask import request
from functools import wraps


def require_user(f):
    """
        This method add the user kwarg to the wrapped method. Will abort
        with a 401 if no Auth Key is present.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        kwargs['user'] = User(request.headers.get('X-Auth-Token', None))
        # TODO: Validate they are a real user
        return f(*args, **kwargs)

    return wrapper
