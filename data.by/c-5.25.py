def remove_all(data,value):
    
    new_list=[]
    for i in (data):
        if i != value:
            new_list.append(i)
    data[:]= new_list
ashraf=[1,4,5,4,5,5,4,8,6,3,7,8,0,8]
remove_all(ashraf,5)
print(ashraf)        
remove_all(ashraf,4)
print(ashraf)
remove_all(ashraf,8)
print(ashraf)
print()
                
                