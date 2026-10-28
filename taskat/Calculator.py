while True:
   question = input("Welcome to the calculator app Do you want to perform any calculation?(yes or no):").strip().lower()
   if question == "no":
      print("calcolator stop ")
      break     
   num_1=(input("Enter your first number:"))
   print("(^),(*),(/),(-),(+)")
   operator=input("Enter your operator:")
   num_2=(input("Enter your second number:"))
   try:
     num1=float(num_1)
   except ValueError:
     print("-----Error please try again-----\n")
     continue
   try:
     num2=float(num_2)
   except ValueError:
      print("-----Error please try again----- \n")
      continue
   if operator=="+":
     result= num1+num2 
   elif operator=="-":
     result= num1-num2
   elif operator=="*":
     result= num1*num2 
   elif operator=="^":
     result= num1**num2 
   elif operator=="/":
      if num2==0:
        print("Cannot divide by zero\n"+"please Try again\n")
        continue
      result= num1/num2
   else:
     print("please try again")
     continue
   print(f"result:{result}\n")   
   i=input("Do you want to perform any other calculations?(yes or no):").strip().lower()
   if i =="yas":
     continue
   print("good bye")
   break   