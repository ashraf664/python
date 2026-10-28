class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_nodes(head):
    
    if head is None:
        return 0
    
    return 1 + count_nodes(head.next)

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(n1)
print( count_nodes(n1))
