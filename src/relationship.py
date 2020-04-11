class Relationship:
    def __init__(self):
        # create proper init signature after checking where it is called
        #def _init_(self, new_name, source, destination, description, vector)
        self.name = None
        self.sourceNode = None
        self.destinationNode = None
        self.description = None
        self.vector = None

    def change_name(self, new_name):
        self.name = new_name

    def change_description(self, new_description):
        self.description = new_description

    def change_source(self, new_source):
        # check if source node is in vector
        self.sourceNode = new_source

    def change_destination(self, new_destination):
        # check if destination node is in vector
        self.destinationNode = new_destination
