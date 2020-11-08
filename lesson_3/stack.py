class Stack:
    def __init__(self):
        self.items = []

    @property
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    @property
    def pop(self):
        return self.items.pop()

    @property
    def peek(self):
        return self.items[len(self.items) - 1]

    @property
    def size(self):
        return len(self.items)


s=Stack()

print(s.items.__class__)
print(s.is_empty)
s.push(4)
s.push('dog')
s.push(True)
print(s.size)
print(s.__dict__)
print(s.is_empty)
s.push(8.4)
print(s.__dict__)
print(s.pop)
print(s.pop)
print(s.size)
print(s.__dict__)
