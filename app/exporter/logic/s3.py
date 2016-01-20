"""
    This module handles all interaction with S3
"""
import uuid
import boto
from boto.s3.key import Key

conn = boto.connect_s3()

bucket = conn.get_bucket("ninja-kpom-mailgun")


def upload(filename):
    k = Key(bucket)
    k.key = "{}.csv".format(uuid.uuid4())
    k.set_contents_from_filename(filename)
    k.set_metadata('Content-Type', "application/csv")
    k.set_acl('public-read')
    return k.generate_url(expires_in=0, query_auth=False)
