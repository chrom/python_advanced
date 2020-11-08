class Queue:
    def __init__(self):
        self.items = []

    @property
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    @property
    def pop(self):
        return self.items.pop(0)


    @property
    def size(self):
        return len(self.items)


queue = Queue()
queue.push("query")
queue.push("it")
queue.push("is")
queue.push("simple")
print(queue.__dict__)

print(queue.pop)
print(queue.__dict__)

