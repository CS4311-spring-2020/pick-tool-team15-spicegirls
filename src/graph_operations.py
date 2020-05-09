import json


class GraphOperations:
    def __init__(self):
        self.flag = 0

    def graph_from_raw_vector(vector):
        empty = {"name": vector['name'], "graph_type": 0, "kwargs": {}, "nodes": [], "edges": []}
        for entry in vector['entries']:
            tempEmptyEntry = {
                        "name": str(entry['id']),
                        "kwargs": {
                            "label": str(entry['name']),
                            "shape": "circle",
                            "width": 1
                        }
                    }
            empty["nodes"].append(tempEmptyEntry)
        for edge in vector['relationships']:
            tempEdge = {
                "source": str(edge['source']),
                "dest": str(edge['destination']),
                "kwargs": {}
            }
            empty["edges"].append(tempEdge)
        y = json.dumps(empty)
        f = open("../Resouces/LocalGraphs/" + vector['name'] + ".json", "w")
        f.write(str(y))
        f.close()

    def graph_from_vector(vector):
        empty = {"name": vector['name'], "graph_type": 0, "kwargs": {}, "nodes": [], "edges": []}
        for entry in vector.nodes:
            tempEmptyEntry = {
                        "name": str(entry.number),
                        "kwargs": {
                            "label": str(entry.content),
                            "shape": "circle",
                            "width": 1
                        }
                    }
            empty["nodes"].append(tempEmptyEntry)
        y = json.dumps(empty)
        f = open("../Resouces/LocalGraphs/" + vector.name+ ".json", "w")
        f.write(str(y))
        f.close()
