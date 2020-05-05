from pymongo import MongoClient
from random import randint


client = MongoClient(port=27017)
db = client.vector


def create_log_entry(content, time_stamp, host, source, source_type):
    db.log_entries.insert_one({'content': content, 'time_stamp': time_stamp, 'host': host, 'source': source,
                               'source_type': source_type})
    return True

