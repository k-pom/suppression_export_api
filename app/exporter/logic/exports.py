from exporter.db import exports
from exporter.models.export import Export
from uuid import uuid4


def list(user, domain):
    export_list = exports.find({
        'domain': domain,
        'user': user.hashed_key
    })
    print({
        'domain': domain,
        'user': user.hashed_key
    })
    return [Export(e) for e in export_list]


def create(user, domain, export_type):
    new_export = Export({
        "domain": domain,
        "user": user.hashed_key,
        "type": export_type,
        "status": "pending",
        "id": str(uuid4())
    })

    exports.insert_one(new_export.serialize())

    return new_export


def delete(user, id):
    exports.delete_one({
        'user': user.hashed_key,
        'id': id
    })
