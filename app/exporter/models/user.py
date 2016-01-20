"""
    This is the model class for an user.
"""

from flask import abort


class User():

    def __init__(self, key):
        if key is None:
            abort(401)

        # TODO: Validate the key

        self.key = key
