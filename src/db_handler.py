import json
from random import randint
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
        self.db.log_entries.insert_one({'id': number,'content': content, 'time_stamp': time_stamp, 'host': host, 'source': source,
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

    def get_vector_from_name(self, name):
        cursor = self.db.vectors.find({'name': name})
        return cursor

    def get_all_vectors_raw(self):
        cursor = self.db.vectors.find({})
        return list(cursor)

    def get_all_vectors(self):
        return ''
