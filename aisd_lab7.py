from enum import Enum
from typing import Any, Optional, Dict, List, Callable
import kolejka_fifo as fifo

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
        index = len(self.adjacencies)+1
        self.adjacencies[Vertex(data, index)] = []
    
    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if source not in self.adjacencies:
            self.adjacencies[source] = []
        self.adjacencies[source].append(Edge(source, destination, weight))
    
    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if source.data not in self.adjacencies:
            self.adjacencies[source] = []
        self.adjacencies[source].append(Edge(source, destination, weight))
        if destination not in self.adjacencies:
            self.adjacencies[destination] = []
        self.adjacencies[destination].append(Edge(destination, source, weight))
    
    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge == 1: # directed
            self.add_directed_edge(source, destination, weight)
        else: # undirected
            self.add_undirected_edge(source, destination, weight)
        
    def traverse_breadth_first(self, visit: Callable[[Any], None]):
        visited = []
        que = fifo.Queue()
        visit(self.adjacencies[0])
        visited.append(self.adjacencies[0])
        que.enqueue(self.adjacencies[0])
        while len(que) != 0:
            v = que.dequeue()
            if v not in visited:
                visit(v)
                visited.append(v)
                for neighbour in self.adjacencies[v]:
                    que.enqueue(neighbour)

    def traverse_depth_first(self, visit: Callable[[Any], None]):
        pass

    def show(self):
        pass

    def print(self):
        for data in self.adjacencies:
            print(data, "---->", self.adjacencies[data], sep=" ")  

def _visit(vertex: Vertex):
    print(vertex)

graf = Graph()