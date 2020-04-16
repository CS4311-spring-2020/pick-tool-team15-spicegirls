class Vector:
    def __init__(self):
        self.name = None
        self.description = None
        self.start = None
        self.end = None
        self.nodes = []
        self.relationships = []

    def change_name(self, new_name):
        self.name = new_name

    def change_description(self, new_description):
        self.description = new_description

    def change_destination(self, new_destination):
        self.name = new_destination

    def change_start(self, new_start):
        self.start = new_start

    def change_end(self, new_end):
        self.end = new_end

    def add_node(self, new_node):
        self.nodes.append(new_node)

    def add_relationship(self, new_name, new_source, new_destination, new_description):
        try:
            self.nodes.index(new_source)
            self.nodes.index(new_destination)
            self.relationships.add((new_name, new_source, new_destination, new_description, self))
        except ValueError:
            pass

    def del_node(self, node):
        try:
            self.nodes.remove(node)
        except ValueError:
            pass

    def del_relationship(self, relationship):
        try:
            self.relationships.remove(relationship)
        except ValueError:
            pass
