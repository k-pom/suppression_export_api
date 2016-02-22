"""
    This module contains all business logic around exports, including
    validating ownership, creating new models, and processing pending
    exports
"""
import os
import csv
from uuid import uuid4

from exporter.db import exports
from exporter.models.export import Export
from exporter.logic import mailgun
from exporter.logic import s3
from flask import abort


def get(user, id):
    export = exports.find_one(Export.key(user, id))
    return Export(export)


def list_exports(api_key, domain):
    export_list = exports.find({
        'domain': domain,
        'user': api_key
    })
    return [Export(e) for e in export_list]


def create(api_key, domain, export_type):

    if export_type not in Export.TYPES:
        abort(400)

    print(api_key)
    print("JDFKDLJFLSDJFLDSJFLDKSJFLSD")
    new_export = Export({
        "domain": domain,
        "user": api_key,
        "type": export_type,
        "status": "pending",
        "id": str(uuid4())
    })

    exports.insert_one(new_export.serialize())

    return new_export


def process_pending():
    for e in exports.find({'status': "pending"}):
        try:
            export = Export(e)
            export.status = 'processing'
            exports.update(export.key, export.serialize())
            create_file(export)
        except Exception as e:
            export.status = 'error'
            exports.update(export.key, export.serialize())
            print(str(e))  # Keep processing files, but log it

def create_file(export):
    """
        This creates the export file for a given export. This creates
        a temp file, downloads all suppressions, writing them to the
        temp file. After it is complete is uploads the file to s3, and
        updates the export record in the database.
    """
    filename = '/tmp/{}-{}.csv'.format(export.domain, uuid4())
    headers = False
    total = 0
    with open(filename, 'w') as fp:
        csv_writer = csv.writer(fp)
        try:
            response = mailgun.list_suppressions(export)

            while response['items']:
                for item in response['items']:
                    if not headers:
                        headers = list(item.keys())
                        csv_writer.writerow(headers)

                    total += 1
                    csv_writer.writerow([item[h] for h in headers])

                response = mailgun.list_suppressions(export, response['paging']['next'])

            export.filename = s3.upload(filename)
            export.status = "completed"
            export.total = total
            exports.update(export.key, export.serialize())
        finally:
            os.remove(filename)


def delete(api_key, id):
    exports.delete_one(Export.key(api_key, id))
