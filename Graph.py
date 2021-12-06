# Graph data structure. See documentation for more information and analysis.

# The methods for this data structure all have constant O(1) space and time complexity because they involve simple insertions and appends into dictionaries and lists.

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edges = {}

    def add_vertex(self, v):
        self.adjacency_list[v] = []
    
    def add_edge(self, v1, v2, d):
        self.adjacency_list[v1].append(v2)
        self.adjacency_list[v2].append(v1)
        self.edges[v1, v2] = d
        self.edges[v2, v1] = d
