import heapq

ashraf = []

def add(key, value):
    heapq.heappush(ashraf, (key, value))

def remove_min():
    return heapq.heappop(ashraf)


add(5, "A")
add(4, "B")
add(7, "F")
add(1, "D")
print("removeMin:", remove_min())   

add(3, "J")
add(6, "L")
print("removeMin:", remove_min())   
print("removeMin:", remove_min())   

add(8, "G")
print("removeMin:", remove_min())   

add(2, "H")
print("removeMin:", remove_min())   
print("removeMin:", remove_min())   
