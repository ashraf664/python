file_name="study_plan.txt"
 
def add_plan():
    try:
        with open(file_name, "r") as f:
            return [line.strip().split("|")for line in f]
    except FileNotFoundError:
        return []
    
def save_plan(plan):
    with open(file_name, "w") as f:
        for topic, status in plan:
            f.write(f"{topic}|{status}\n")

def show_plan(plan):
    if not plan:
        print("There are no plans yet")
    else:
        for i in range(len(plan)):
            topic , status = plan[i]
            print(f"{i+1}.{topic}-{status}")

def main():
    plan=add_plan()
    while True:
        print("\n 1) Add \n 2) Show \n 3) Complete \n 4) Delete \n 5) Exit")
        choice=input("choice number:")
        if choice=="1":
            topic=input("enter your topic" )
            plan.append([topic,"incomplete"])
        elif choice=="2":
            show_plan(plan)
        elif choice=="3":
            show_plan(plan)
            i=int(input("enter topic number"))-1
            if 0 <= i <len(plan):
                plan[i][1]="complet"
        elif choice=="4":
            show_plan(plan)
            i=int(input("enter topic numper to delete:"))-1
            if 0 <= i < len (plan):
                plan.pop(i)
        elif choice=="5":
            save_plan(plan)
            print("plan saved")
            break
        else:
            print("try again")    

main() 