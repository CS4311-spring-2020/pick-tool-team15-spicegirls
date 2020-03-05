from __future__ import absolute_import
from __future__ import print_function
import sys, os
import splunklib.client as client
import asyncio, concurrent.futures


class SplunkHandler:
    def __init__(self):
        try:
            self.service = client.connect(
                host="localhost",
                port=8089,
                username="leochoa2",
                password="n9cErPvGV2ds5A^")

        except Exception as Error:
            print("error connecting to splunk")
            exit(1)

    #assuming file is absolute path
    #need name of index being added to
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

    def create_jobs(self):

        kwargs_blockingsearch = {"exec_mode": "blocking"}
        searchquery_blocking = "search * | head 100"

        # A blocking search returns the job's SID when the search is done
        job = self.service.jobs.create(searchquery_blocking, **kwargs_blockingsearch)
        self.print_jobs()
    def create_new_user(self,username,password,role,fullname):
        newuser = self.service.users.create(username=username, password=password, roles=role, realname=fullname)

splunkHandler = SplunkHandler()
splunkHandler.print_indexes()
#splunkHandler.create_new_user("testAdmin", "password", "admin", "testAdmin")
splunkHandler.print_users()
#splunkHandler.add_file("main","/Users/dima/Desktop/pick-tool-team15-spicegirls/src/testing/testing.txt")