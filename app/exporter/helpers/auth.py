"""
Auth related helper methods
"""
from flask import abort
from flask import request
from functools import wraps


def require_user(f):
    """
        This method add the user kwarg to the wrapped method. Will abort
        with a 401 if no Auth Key is present.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        kwargs['api_key'] = request.headers.get('X-Auth-Token', None)

        if kwargs['api_key'] is None:
            abort(401)
            
        # TODO: Validate they are a real user
        return f(*args, **kwargs)

    return wrapper
