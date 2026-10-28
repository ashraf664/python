def remove_duplicates(A):
    S = set()     
    result = []    

    for item in A:
        if item not in S:
            S.add(item)
            result.append(item)

    return result
