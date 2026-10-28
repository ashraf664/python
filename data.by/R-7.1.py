class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def second_to_last(head):
    if head is None:
        return None
    
    if head.next is None:
        return None

    current = head
    while current.next.next is not None:
        current = current.next

    return current

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
result = second_to_last(n1)

print(result.data)
