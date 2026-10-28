from collections import deque

def merge(q1, q2):
    result = deque()
    while q1 and q2:
        if q1[0] <= q2[0]:
            result.append(q1.popleft())
        else:
            result.append(q2.popleft())
    result.extend(q1)
    result.extend(q2)
    return result

def bottom_up_merge_sort(A):
    
    queues = [deque([item]) for item in A]
    
    while len(queues) > 1:
        new_queues = []
        
        for i in range(0, len(queues), 2):
            if i + 1 < len(queues):
                merged = merge(queues[i], queues[i+1])
                new_queues.append(merged)
            else:
                new_queues.append(queues[i])
        
        queues = new_queues
    
    return list(queues[0]) if queues else []


A = [7, 3, 9, 1, 4, 2,5,10]
sorted_A = bottom_up_merge_sort(A)
print("Before:", A)
print("After :", sorted_A)