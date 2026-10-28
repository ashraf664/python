class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,items):
        self.items.append(items)
    def dequeue(self):
        return self.items.pop(0)
    def is_empty(self):
        return(len(self.items))==0
    def __str__(self):
        return str(self.items)
def transfer(S,T):
    while not S.is_empty():
        T.enqueue(S.dequeue())

S=Queue()
T=Queue()
for i in [1,2,3,4,5,6]:
    S.enqueue(i)
print("Queue S Before",S)
transfer(S,T)


print("Queue S After:",S)
print("Queue T  :",T)           



