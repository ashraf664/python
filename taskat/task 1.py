def average(gr):
     total1=sum(gr)
     total2=len(gr)
     return  total1/total2  
while True:
 name =input("enter your name:")
 num=int(input("enter thr number for subject:"))
 gr=[]
 for i in range (num):
  grades = float(input("entar your grade"))
 gr.append(grades)
 average = average(gr)
 print(f"hallo {name}")
 print(f" your totale average {average}")
 if average>=50:
     print("passed")
 else:
  print("failed")
 x=input("Do you want to enter details for another student?(true or false)=")
 if x!="true":
  break