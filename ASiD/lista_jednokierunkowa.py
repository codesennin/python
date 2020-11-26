from typing import Any
class Node:
    value: Any
    next: 'Node'

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        if(self.next == None):
            return f'{self.value}'
        return f'{self.value} -> {self.next}'

class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, firstval):
        firstobj = Node(value = firstval)
        firstobj.next = self.head
        self.head = firstobj
        if(self.tail == None):
            self.tail = firstobj
    
    def append(self, lastval):
        lastobj = Node(value = lastval)
        if(self.head == None):
            self.push(lastval)
        else:
            self.tail.next = lastobj
            self.tail = lastobj
    
    def node(self, at):
        temp = self.head
        for x in range(at):
            if(temp.next != None):
                temp = temp.next
            else:
                return None
        return temp

    def insert(self, betweenval, after):
        betweenobj = Node(value = betweenval)
        betweenobj.next = after.next
        after.next = betweenobj

    def pop(self):
        first = self.head
        self.head = self.head.next
        return first.value

    def remove_last(self):
        last = self.tail
        new_last = self.head
        while(new_last.next.next != None):
            new_last = new_last.next
        self.tail = new_last
        self.tail.next = None
        return last.value

    def remove(self, after):
        after.next = after.next.next
    
    def __repr__(self):
        return f'{self.head}'
    

    
test_ = LinkedList()
print(test_)
assert test_.head == None

test_.push(1)
test_.push(0)
print(test_)
assert str(test_) == '0 -> 1'

test_.append(9)
test_.append(10)
print(test_)
assert str(test_) == '0 -> 1 -> 9 -> 10'

between = test_.node(at=1)
test_.insert(5, between)
print(test_)
assert str(test_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = test_.node(at=0)
returned_first_element = test_.pop()
print(test_)
assert first_element.value == returned_first_element

last_element = test_.node(at=3)
returned_last_element = test_.remove_last()
print(test_)
assert last_element.value == returned_last_element
assert str(test_) == '1 -> 5 -> 9'

second_node = test_.node(at=1)
test_.remove(second_node)
print(test_)
assert str(test_) == '1 -> 5'