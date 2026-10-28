def duplicate_num(A):    
    number=set()
    for num in(A):
      if num in number:
         return num
      number.add(num)
    return "no repeated number"
   
A = list(map(int, input("Enter the numbers + space =").split()))

print("The repeated number =", duplicate_num(A))
