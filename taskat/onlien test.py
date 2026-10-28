def create_plan():
    days = int(input("Enter the number of days: "))
    the_topics = int(input("Enter the number of topics: "))
    topics = []

    for i in range(the_topics):
        topic = input(f"Enter topic {i+1}: ")
        topics.append(topic)

    rule = the_topics // days
    extra = the_topics % days
    plan = []
    index = 0
    d = 0

    while d < days:
        count = rule + (1 if d < extra else 0)
        day_topics = topics[index:index+count]
        plan.append(day_topics)
        index += count
        d += 1

    print("\n Your Study Plan:")
    d = 0
    while d < len(plan):
        print(f"Day {d+1}: {', '.join(plan[d])}")
        d += 1
    
    save = input("\nDo you want to save the plan to a file? (yes/no): ").strip().lower()
    if save != "no":
        with open("study_plan.txt", "w",) as f:
            f.write(" Study Plan\n")
            d = 0
            while d < len(plan):
                f.write(f"Day {d+1}: {', '.join(plan[d])}\n")
                d += 1
        print(" Plan saved to 'study_plan.txt'")
create_plan()        