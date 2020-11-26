from typing import Any, List
from binarytree import build
import queue

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'
    
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
    
    def min(self):
        min = self.value
        temp = self
        while temp.left_child is not None:
            temp = temp.left_child
            if temp.value < min:
                min = temp.value
        return min

class BinarySearchTree:
    root: BinaryNode

    def __init__(self, value = None):
        self.root = BinaryNode(value)
    
    def insert(self, value: Any):
        self._insert(self.root, value)
    
    def _insert(self, node: BinaryNode, value: Any):
        if value < node.value:
            if node.left_child is None:
                node.left_child = BinaryNode(value)
            else:
                self._insert(node.left_child, value)
        else:
            if node.right_child is None:
                node.right_child = BinaryNode(value)
            else:
                self._insert(node.right_child, value)
    
    def insertlist(self, list: List[Any]):
        for value in list:
            self.insert(value)
        
    def contains(self, value): # używa get() zrobiony na potrzeby wyświetlania
        nodes = []
        self.get(nodes)        # nie taki ten get() zły jak się wydawał wcześniej
        for node in nodes:     # przydatny przynajmniej
            if node is not None:
                if node.value == value:
                    return True
        return False
    
    def remove(self, value: Any):
        self.root = self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value: Any):
        if node.value == value:
            if node.left_child is None and node.right_child is None:
                node.value = None
            elif node.left_child is None and node.right_child is not None:
                return node.right_child
            elif node.left_child is not None and node.right_child is None:
                return node.left_child
            node.value = node.right_child.min().value
            node.right_child = self._remove(node.right_child, node.value)
        elif value < node.value:
            self._remove(node.left_child, value)
        else:
            self._remove(node.right_child, value)
        
    def get(self, nodes):
        que = queue.Queue()
        nodes.append(self.root)
        que.put(self.root)
        while que.empty() == False:
            temp = que.get()
            for child in [temp.left_child, temp.right_child]:
                if child is not None:
                    nodes.append(child)
                    que.put(child)
                else:
                    nodes.append(None)

    # show() i get() zakoszone z binary_tree, bo po co robić 2x to samo
    def show(self):
        nodes = []
        self.get(nodes)
        values = []
        for node in nodes:
            if node != None:
                values.append(node.value)
            else:
                values.append(None)
        print(build(values))


drzewo = BinarySearchTree(5)
drzewo.insert(2)
drzewo.insert(7)
drzewo.insert(3)
drzewo.insert(1)
drzewo.insert(6)
drzewo.insert(9)
drzewo.insert(10)
drzewo.insert(4)
drzewo.insert(8)

drzewo.show()
drzewo.remove(10)

# print(drzewo.contains(4))
# print(drzewo.contains(21))