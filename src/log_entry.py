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
    return False


def change_log_entry_content(_id, new_content):
    if db.log_entries.update_one({'_id': ObjectId(str(_id))}, {'$set': {'content': new_content}}).modified_count is 1:
        return True
    return False


def change_log_entry_timestamp(_id, new_timestamp):
    if db.log_entries.update_one({'_id': ObjectId(str(_id))}, {'$set': {'time_stamp': new_timestamp}}).modified_count is 1:
        return True
    return False


def change_log_entry_host(_id, new_host):
    if db.log_entries.update_one({'_id': ObjectId(str(_id))}, {'$set': {'host': new_host}}).modified_count is 1:
        return True
    return False


def change_log_entry_source(_id, new_source):
    if db.log_entries.update_one({'_id': ObjectId(str(_id))}, {'$set': {'source': new_source}}).modified_count is 1:
        return True
    return False


def change_log_entry_source_type(_id, new_source_type):
    if db.log_entries.update_one({'_id': ObjectId(str(_id))}, {'$set': {'source_type': new_source_type}}).modified_count \
            is 1:
        return True
    return False
