from typing import Any, Callable
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

    def is_leaf(self):
        if self.left_child == None and self.right_child == None:
            return True
        return False
    
    def add_left_child(self, value: Any):
        if self.left_child == None:
            self.left_child = BinaryNode(value)
        else:
            print("Lewe dziecko już istnieje")

    def add_rigth_child(self, value: Any):
        if self.right_child is None:
            self.right_child = BinaryNode(value)
        else:
            print("Prawe dziecko już istnieje")

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)
    
    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child != None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child != None:
            self.right_child.traverse_pre_order(visit)  

    def __repr__(self):
        return f'{self.value}'

class BinaryTree:
    root: BinaryNode

    def __init__(self, value = None):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    # METODA PRZECHODZI PO DRZEWIE METODĄ FOR_EACH_LEVEL_ORDER
    # I DODAJE DO LISTY NODY 
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

    # PRZY UŻYCIU BIBLIOTEKI ZEWNĘRZNEJ BINARYTREE BUDUJE DRZEWO 
    # Z LISTY UTWORZONEJ METODĄ GET I WYŚWIETLA DRZEWO METODĄ WBUDOWANĄ
    def show(self):
        nodes = []
        self.get(nodes)
        # print(nodes)
        values = []
        for node in nodes:
            if node != None:
                values.append(node.value)
            else:
                values.append(None)
        print(build(values))
        
def _visit(node: BinaryNode):
    print(node)

# DEKLARACJA DRZEWA
tree = BinaryTree(10)
tree.root.add_left_child(9)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_rigth_child(3)
tree.root.add_rigth_child(2)
tree.root.right_child.add_left_child(4)
tree.root.right_child.add_rigth_child(6)
tree.root.right_child.right_child.add_left_child(7)

# CZY DOBRZE WYŚWIETLA PRZEJŚCIA
# tree.traverse_in_order(_visit)
# tree.traverse_post_order(_visit)
# tree.traverse_pre_order(_visit)

# ASSERTY
assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True

# WYŚWIETLENIE DRZEWA
tree.show()