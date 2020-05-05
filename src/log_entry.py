from pymongo import MongoClient
from bson import ObjectId


client = MongoClient(port=27017)
db = client.vector


def create_log_entry(content, time_stamp, host, source, source_type):
    db.log_entries.insert_one({'content': content, 'time_stamp': time_stamp, 'host': host, 'source': source,
                               'source_type': source_type})
    return True


def delete_log_entry(_id):
    if db.log_entries.delete_one({'_id': ObjectId(str(_id))}).deleted_count is 1:
        return True


def change_log_entry_content(_id, new_content):
    if db.log_entries.update_one({'_id': ObjectId(str(_id))},{'$set': {'content': new_content}}).modified_count is 1:
        return True

