from pymongo import MongoClient
import os

client = MongoClient(os.environ["DB_HOST"])
client.suppressions.authenticate(os.environ["DB_USER"], os.environ["DB_PASS"])

db = client.suppressions
exports = db.exports
