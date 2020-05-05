from __future__ import absolute_import
from __future__ import print_function
import sys, os
import splunklib.client as client
import asyncio, concurrent.futures
from splunklib import results
import log_entry

class SplunkHandler:
    def __init__(self, host, port, index, username, password):

        self.host = host
        self.port = port
        self.index = index
        self.username = username
        self.password = password
        try:
            self.service = client.connect(host=self.host, port=self.port, username=self.username, password=self.password)
        except Exception as e:
            print(str(e))
        
    def add_file(self, index, file):

        myindex = self.service.indexes[index]
        myindex.upload(file)

    def add_index(self,index):

        self.service.indexes.create(index)

    def print_users(self):
        kwargs = {"sort_key": "realname", "sort_dir": "asc"}
        users = self.service.users.list(count=-1, **kwargs)
        print(self.service.username)
        # Print the users' real names, usernames, and roles
        print("Users:")
        for user in users:
            print("%s (%s)" % (user.realname, user.name))
            for role in user.role_entities:
                print(" - ", role.name)

    def print_indexes(self):
        indexes = self.service.indexes
        for index in indexes:
            count = index["totalEventCount"]
            print("%s (events: %s)" % (index.name, count))

    def print_jobs(self):
        jobs = self.service.jobs
        print("there are %d jobs :", len(jobs))

    #doesnt work yet
    def create_jobs(self):

        kwargs_blockingsearch = {"exec_mode": "blocking"}
        searchquery_blocking = "search * | head 100"

        # A blocking search returns the job's SID when the search is done
        job = self.service.jobs.create(searchquery_blocking, **kwargs_blockingsearch)
        self.print_jobs()

    def create_new_user(self,username,password,role,fullname):
        newuser = self.service.users.create(username=username, password=password, roles=role, realname=fullname)

    def add_directory(self, path):
        inputs = self.service.inputs
        newInput = inputs.create(path, "monitor")

    def print_inputs(self):
        # Get the collection of data inputs
        inputs = self.service.inputs

        # List the inputs and kind
        for item in inputs:
            print("%s (%s)" % (item.name, item.kind))


    def download_log_files(self):
        jobs = self.service.jobs
        blocking_search = {"exec_mode": "blocking"}
        query = "search | head 5"
        job = jobs.create(query, **blocking_search)
        job_results = results.ResultsReader(job.results(count=5))
        for result in job_results:
            if True:
                log_entry.create_log_entry(result['_raw'], result['_indextime'], result['host'], result['source'], result['sourcetype'])


    def cleanse(self,file):
        return self.cleanse.cleanse(file)

    def validate(self,file,event_start, event_end):
        self.validate.startTimestamp = event_start
        self.validate.endTimestamp = event_end
        return self.validate.validate(file)

if __name__ == '__main__':
    client = SplunkHandler('localhost', 8089, 'main', 'SpiceGirls', '@DimaAbdelJaber1234@')
    client.add_file("main","/Users/dima/Desktop/pick-tool-team15-spicegirls/src/sample.txt")
    client.download_log_files()
    print(client.download_log_files())
