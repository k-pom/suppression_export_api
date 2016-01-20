"""
    This handles all database connections and credentials
"""
import os
from pymongo import MongoClient

client = MongoClient(os.environ["DB_HOST"])
client.suppressions.authenticate(os.environ["DB_USER"], os.environ["DB_PASS"])

db = client.suppressions
exports = db.exports
