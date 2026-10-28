class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

def transfer(S, T):
    
    while not S.is_empty():
        T.push(S.pop())

n = input("enter stack (S) by space: ")
num = list(map(int, n.split()))

S = Stack()
for i in num:
    S.push(i)

T = Stack()
transfer(S, T)

print("Stack T:", T)
