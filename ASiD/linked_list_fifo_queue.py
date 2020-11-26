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
        return f'{self.value}, {self.next}'

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
    
    def __len__(self):
        len = 0
        temp = self.head
        while(temp != None):
            temp = temp.next
            len += 1
        return len

class Queue:
    queue: 'LinekdList'

    def __init__(self):
        self.queue = LinkedList()

    def __len__(self):
        return len(self.queue)

    def peek(self):
        return self.queue.head.value

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        return self.queue.pop()
    
    def __repr__(self):
        if (self.queue.head.next == None):
            return f'{self.queue.head.value}'
        return f'{self.queue.head.value}, {self.queue.head.next}'

#################
#### EXAMPLE ####
#################

# queue = Queue()
# print(len(queue))
# assert len(queue) == 0

# queue.enqueue('client1')
# queue.enqueue('client2')
# queue.enqueue('client3')
# print(queue)
# print(len(queue))
# assert str(queue) == 'client1, client2, client3'

# client_first = queue.dequeue()
# print(client_first)
# assert client_first == 'client1'
# print(queue)
# assert str(queue) == 'client2, client3'
# print(len(queue))
# assert len(queue) == 2