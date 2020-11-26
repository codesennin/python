from typing import Any

class Node:
    value: Any
    next: 'Node'
    
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        if(self.next==None):
            return f'{self.value}'
        return f'{self.value} -> {self.next}' 
    
class LinkedList:
    head = None
    tail = None

    def push(self, nvalue):
        nobject=Node(value=nvalue)
        nobject.next=self.head
        self.head=nobject
        if(self.tail==None):
            self.tail=nobject
    
    def append(self, nvalue):
        nobject=Node(value=nvalue)
        self.tail.next=nobject
        self.tail=nobject
        if(self.head==None):
            self.head=nobject
    
    def __repr__(self):
        return f'{self.head}'

list_ = LinkedList()
print(list_)
assert list_.head == None

list_.push(1)
list_.push(0)
print(list_)
assert str(list_) == '0 -> 1'