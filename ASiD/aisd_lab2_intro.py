class A:
    attr1: int
    attr2: int

    def __init__(self, attr1=10, attr2=20):
        self.attr1 = attr1
        self.attr2 = attr2

    def sum(self):
        return self.attr1 + self.attr2

    def inc_attr1(self, value):
        self.attr1 += value
    
    def __repr__(self):
        return f'attr1: {self.attr1}, attr2: {self.attr2}'

    def __len__(self):
        return 2
    

obj1 = A(attr1=1)
obj2 = A(attr2=6)

obj2.inc_attr1(1)
print(f'obj2 attr1: {obj2.attr1}')

print(obj1)
print(obj2)

print(len(obj1))

# assercja przerywa działanie programu jeżeli wartość będzie false
assert obj1.attr1 == 1 and obj1.attr2 == 21
