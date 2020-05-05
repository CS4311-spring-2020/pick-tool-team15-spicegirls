import json

from pymongo import MongoClient


class DBHandler:
    def __init__(self):
        # Needs connection exception handling
        self.client = MongoClient(port=27017)
        self.db = self.client.PICK

    def create_log_entry(self, content, time_stamp, host, source, source_type):
        self.db.log_entries.insert_one({'content': content, 'time_stamp': time_stamp, 'host': host, 'source': source,
                                   'source_type': source_type})

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

    def get_all_vectors_raw(self):
        cursor = self.db.vectors.find({})
        return list(cursor)

    def get_all_vectors(self):
        return ''
