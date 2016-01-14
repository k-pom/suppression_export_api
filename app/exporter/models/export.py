from datetime import datetime


class Export():

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
