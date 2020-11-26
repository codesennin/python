from enum import Enum
from typing import Any, Optional, Dict, List, Callable
from ASiD import linked_list_fifo_queue as fifo

class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    data: Any
    index: int
    def __init__(self, data: Any, index: int):
        self.data = data
        self.index = index
    
    def __repr__(self):
        return f"{self.index}: {self.data}"

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]
    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.source = source
        self.destination = destination
        self.weight = weight
    
    def __repr__(self):
        return f"{self.destination}"

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]
    def __init__(self):
        self.adjacencies = {}
    
    def create_vertex(self, data: Any):
        index = len(self.adjacencies)
        self.adjacencies[Vertex(data, index)] = []
    
    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))
    
    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))
    
    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge == 1: # directed
            self.add_directed_edge(source, destination, weight)
        else: # undirected
            self.add_undirected_edge(source, destination, weight)
        
    def traverse_breadth_first(self, visit: Callable[[Any], None]):
        keys = self.getVertexs()
        visited = []
        que = fifo.Queue()
        que.enqueue(keys[0])
        while len(que) != 0:
            v = que.dequeue()
            visit(v)
            visited.append(v)
            for neighbour in self.adjacencies[v]:
                if neighbour.destination not in visited:
                    que.enqueue(neighbour.destination)

    def traverse_depth_first(self, visit: Callable[[Any], None]):
        pass

    def show(self):
        pass

    def print(self):
        for data in self.adjacencies:
            print(data, "---->", self.adjacencies[data], sep=" ")  
    
    def getVertexs(self):
        keys = []
        for key in self.adjacencies.keys():
            keys.append(key)
        return keys

def _visit(vertex: Vertex):
    print(vertex)

#################
#### EXAMPLE ####
#################

graph = Graph()
graph.create_vertex("v0")
graph.create_vertex("v1")
graph.create_vertex("v2")
graph.create_vertex("v3")
graph.create_vertex("v4")
graph.create_vertex("v5")

vertexs = graph.getVertexs()

graph.add(2, vertexs[0], vertexs[1])
graph.add(2, vertexs[0], vertexs[5])
graph.add(2, vertexs[5], vertexs[2])
graph.add(2, vertexs[5], vertexs[1])
graph.add(2, vertexs[2], vertexs[3])
graph.add(2, vertexs[2], vertexs[1])
graph.add(2, vertexs[3], vertexs[4])
graph.add(2, vertexs[4], vertexs[5])
graph.add(2, vertexs[4], vertexs[1])

graph.print()
# graph.traverse_breadth_first(_visit)