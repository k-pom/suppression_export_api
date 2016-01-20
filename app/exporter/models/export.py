"""
    This is the model class for an export.
"""

from datetime import datetime


class Export():

    TYPES = ['bounces', 'unsubscribes', 'complaints']

    def __init__(self, raw_data):
        self.id = raw_data.get("id", None)
        self.domain = raw_data['domain']
        self.type = raw_data['type']
        self.status = raw_data['status']
        self.user = raw_data['user']
        self.filename = raw_data.get('filename', None)
        self.total = raw_data.get('total', None)

        if "created_at" in raw_data:
            self.created_at = raw_data['created_at']
        else:
            self.created_at = datetime.now().isoformat()

        self.key = {
            'user': self.user,
            'id': self.id
        }

    @classmethod
    def key(cls, user, id):
        return {
            'user': api_key,
            'id': id
        }

    def serialize(self):
        return {
            "id": self.id,
            "domain": self.domain,
            "type": self.type,
            "status": self.status,
            "user": self.user,
            "filename": self.filename,
            "total": self.total,
            "created_at": self.created_at
        }
