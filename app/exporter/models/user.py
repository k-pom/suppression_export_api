import hashlib
from flask import abort


class User():

    def __init__(self, key):
        if key is None:
            abort(401)

        self.key = key
        self.hashed_key = hashlib.sha256(key.encode('utf-8')).hexdigest()

    def serialize(self):
        return {
            "hashed_key": self.hashed_key
        }
