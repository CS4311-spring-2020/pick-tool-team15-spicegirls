from __future__ import absolute_import
from __future__ import print_function
import sys, os
import splunklib.client as client
import asyncio, concurrent.futures
import splunklib.results as results
from splunklib.binding import AuthenticationError
import os
from LogEntry import LogEntry
from cleansing import Cleanser
from Validate import Validator
from transcription import convert
import datetime
from time import sleep
import json

class SplunkHandler():
    def __init__(self, host, port, index, username, password):
        self.host = host
        self.port = port
        self.index = index
        self.username = username
        self.password = password
        self.entries = list()
        try:
            self.service = client.connect(host=self.host, port=self.port, username=self.username, password=self.password)
        except Exception as e:
            print(str(e))

    def create_index(self, name):
        self.service.indexes.create(name)

    def set_index(self, name):
        self.index = name

    def upload_file(self, path, index):
        ind = self.service.indexes[index]
        try:
            ind.upload(os.path.abspath(path))
        except Exception as e:
            print(str(e))

    def view_indexes(self):
        for index in self.service.indexes:
            print(index.name)

    def get_index(self,index):
        return self.service.indexes.get(index)

    def get_content(self,index):
        self.set_index(index)
        for job in self.service.jobs:
            print(job)

    def download_log_files(self):
        # Retrieve search jobs
        jobs = self.service.jobs

        # blocks until search is finished
        blocking_search = {"exec_mode": "blocking"}
        query = "search | head 5"

        # Create search job
        job = jobs.create(query, **blocking_search)

        # Parse results
        job_results = results.ResultsReader(job.results(count=5))
        i = 0
        for result in job_results:
            if True:
                self.entries.append(LogEntry(i, result['_indextime'], result['_raw'], result['host'], result['source'], result['sourcetype']))
            i += 1
        return self.entries


if __name__ == '__main__':
    #client = SplunkHandler('localhost', 8089, 'one', 'spiceteam', '007dannyd')
    client = SplunkHandler('localhost', 8089, 'test1', 'SpiceGirls', '@DimaAbdelJaber1234@')
    client.view_indexes()
    #client.set_index('test2')
    client.upload_file("sample.txt", 'test2')
    print(client.download_log_files())
    print(client.entries)

