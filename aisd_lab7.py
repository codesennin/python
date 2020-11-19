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
        visit(self.adjacencies[keys[0]])
        visited.append(self.adjacencies[keys[0]])
        que.enqueue(self.adjacencies[keys[0]])
        while len(que) != 0:
            v = que.dequeue()
            if v not in visited:
                visit(v)
                visited.append(v)
                for neighbour in self.adjacencies[keys[v]]:
                    que.enqueue(neighbour)

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

graf = Graph()
graf.create_vertex("v0")
graf.create_vertex("v1")
graf.create_vertex("v2")
graf.create_vertex("v3")
graf.create_vertex("v4")
graf.create_vertex("v5")

wierzcholki = graf.getVertexs()

graf.add(2, wierzcholki[0], wierzcholki[1])
graf.add(2, wierzcholki[0], wierzcholki[5])
graf.add(2, wierzcholki[5], wierzcholki[2])
graf.add(2, wierzcholki[5], wierzcholki[1])
graf.add(2, wierzcholki[2], wierzcholki[3])
graf.add(2, wierzcholki[2], wierzcholki[1])
graf.add(2, wierzcholki[3], wierzcholki[4])
graf.add(2, wierzcholki[4], wierzcholki[5])
graf.add(2, wierzcholki[4], wierzcholki[1])

# graf.print()
graf.traverse_breadth_first(_visit)