import json
from random import randint

from bson import ObjectId
from pymongo import MongoClient


class DBHandler:
    def __init__(self):
        # Needs connection exception handling
        self.client = MongoClient(port=27017)
        self.db = self.client.PICK
        self.collectionList = {'log_entries', 'vectors'}

    # def createDummyData(self):
    #     sources = ['blue', 'red', 'white']
    #     for x in range(1, 50):
    #         entry = {'id': x,
    #                  'content': 'entryData',
    #                  'time_stamp': '2011-08-12 20:17:46',
    #                  'host': 'host',
    #                  'source': sources[randint(0, (len(sources)-1))],
    #                  'source_type': 'source_type'}
    #         self.db.deleteThis.insert_one(entry)

    def get_all_log_entries(self):
        # replace delethis for entries
        cursor = self.db.deleteThis.find({})
        return cursor

    def create_log_entry(self, number, content, time_stamp, host, source, source_type):
        self.db.log_entries.insert_one({'id': number, 'content': content, 'time_stamp': time_stamp, 'host': host,
                                        'source': source, 'source_type': source_type})

    def delete_log_entry(self, _id):
        if self.db.log_entries.delete_one({'_id': ObjectId(str(_id))}).deleted_count == 1:
            return True
        return False

    def change_log_entry_content(self, _id, new_content):
        if self.db.log_entries.update_one({'_id': ObjectId(str(_id))},
                                     {'$set': {'content': new_content}}).modified_count == 1:
            return True
        return False

    def change_log_entry_timestamp(self, _id, new_timestamp):
        if self.db.log_entries.update_one({'_id': ObjectId(str(_id))},
                                     {'$set': {'time_stamp': new_timestamp}}).modified_count == 1:
            return True
        return False

    def change_log_entry_host(self, _id, new_host):
        if self.db.log_entries.update_one({'_id': ObjectId(str(_id))}, {'$set': {'host': new_host}}).modified_count == 1:
            return True
        return False

    def change_log_entry_source(self, _id, new_source):
        if self.db.log_entries.update_one({'_id': ObjectId(str(_id))}, {'$set': {'source': new_source}}).modified_count == 1:
            return True
        return False

    def change_log_entry_source_type(self, _id, new_source_type):
        if self.db.log_entries.update_one({'_id': ObjectId(str(_id))},
                                     {'$set': {'source_type': new_source_type}}).modified_count \
                == 1:
            return True
        return False

    def create_vector_entry(self, jsonFile):
        with open(jsonFile) as f:
            d = json.load(f)
        self.db.vectors.insert_one(d)

    def get_vector_names(self):
        cursor = self.db.vectors.find({})
        names = []
        for vector in cursor:
            if vector['name']:
                names.append(vector['name'])
        return names

    def get_vector_from_name(self, name):
        cursor = self.db.vectors.find({'name': name})
        return cursor

    def get_all_vectors_raw(self):
        cursor = self.db.vectors.find({})
        return list(cursor)

    def get_all_vectors(self):
        return ''

            

