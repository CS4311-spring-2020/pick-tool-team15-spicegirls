from pymongo import MongoClient


class DBHandler:
    def __init__(self):
        # Needs connection exception handling
        self.client = MongoClient(port=27017)
        self.db = self.client.business

    def create_log_entry(self, content, time_stamp, host, source, source_type):
        self.db.log_entries.insert_one({'content': content, 'time_stamp': time_stamp, 'host': host, 'source': source,
                                   'source_type': source_type})

