def remove_all(stack):
    while not  stack:
        return
    stack.pop()
    remove_all(stack)  
ashraf= [1, 2, 3, 4, 5]
print(ashraf)
remove_all(ashraf)
print(ashraf)  
