from typing import Any, List
import  queue

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value = None):
        self.value = value
        self.children = list()

    def is_leaf(self):
        if len(self.children)==0:
            return True
        return False
    
    def add(self, child):
        self.children.append(child)
    
    def for_each_deep_first(self, visit):
        visit(self)
        for child in self.children:
            child.for_each_deep_first(visit)
    
    def for_each_level_order(self, visit):
        que = queue.Queue()
        que.put(self)
        while que.empty()==False:
            temp = que.get()
            visit(temp)
            for child in temp.children:
                que.put(child)
    
    def search(self, value):
        if self.value == value:
            return True
        for child in self.children:
            if child.search(value):
                return True
        return False

    def __repr__(self):
        return f'{self.value}'

class Tree:
    root: TreeNode

    def __init__(self, root = None):
        self.root = root

    def add(self, value: Any, parent_value: Any):
        if self.root.search(parent_value):
            node = TreeNode(value)
            que = queue.Queue()
            que.put(self.root)
            while len(que) == 0:
                temp = que.get()
                if temp.value == parent_value:
                    temp.add(node)
                    break
                for child in temp.children:
                    que.put(child)
        else:
            print("Brak takiej wartości poprzedzającej w drzewie")
    
    def for_each_level_order(self, visit):
        self.root.for_each_level_order(visit)

    def for_each_level_order(self, visit):
        self.root.for_each_level_order(visit)


def _visit(node: TreeNode):
    print(node)


