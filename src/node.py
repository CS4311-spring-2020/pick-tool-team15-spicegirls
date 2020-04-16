class Node:
    def __init__(self):
        # create proper init signature after checking where it is called
        # def _init_(self, new_name, new_icon, new_time_stamp, new_description, log_entry)
        self.name = None
        self.icon = None
        self.time_stamp = None
        self.description = None

    def change_name(self, new_name):
        self.name = new_name

    def change_description(self, new_description):
        self.description = new_description

    def change_icon(self, new_icon):
        # check if icon exists
        self.icon = new_icon

    def change_time_stamp(self, new_time_stamp):
        # check if time stamp is valid
        self.time_stamp = new_time_stamp
