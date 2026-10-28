while True:
 cust_name =input("enter your name:")
 num_prod=int(input("enter thr number for prodact:"))
 sup_total=0
 prod=[]
 for m in range(num_prod):
  print("\nprodact")
  prod_name = input("prodact name:")
  prod_number = int(input("enter the probact num:"))
  prod_rice = float(input("please enter rice:"))
  total = prod_rice*prod_number
  sup_total += total
  prod.append([prod_name,prod_rice,prod_number,total]) 
 tax = sup_total*0.14
 finall_total=sup_total+tax
 print(f"hallo:\t{cust_name}")
 print("----Here is your bill----\n")
 print("Prodacr\tQty\tUnit Price\tTotal")
 print("-------\t---\t----------\t-----")
 for x in prod:
    print(f"{x[0]}\t{x[2]}\t   {x[1]}\t\t{x[3]}\n")

 print(f"Sup Total:{sup_total}\n") 
 print(f"Tax(%14):{tax}\n")
 print(f"Total:{finall_total}\n")
 i = input("Do you need anything else?(yas or no)=")
 if i!="yas":
  print("Good luck")
  break


