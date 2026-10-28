def find_duplicates(value):
    x=set()
    dup=[]
    for i in value:
        if i in x:
            dup.append(i)
        else:
            x.add(i)
    return dup     
ashraf=[3, 1, 5, 3, 7, 2, 5, 9, 8, 1,9,7]            
print(find_duplicates(ashraf))
