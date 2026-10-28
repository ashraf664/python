class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

def remove_all(q):
    while not q.is_empty():
        q.dequeue()

ashraf= Queue()
for x in [1, 2, 3, 4, 5]:
    ashraf.enqueue(x)

print("Queue (ashraf) Before", ashraf)
remove_all(ashraf)
print("Queue (ashraf) Aftar", ashraf)
