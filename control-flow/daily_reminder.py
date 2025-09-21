task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate action today")
        else:
            print(f"'{task}' is a high priority task. Consider completing it soon")
    case "medium":
        if time_bound == "yes":
            print(f"'{task} is a medium priority task that require attention today")
        else:
            print(f"'{task}' is a low priority task. Consider completing it tommorow")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low priority task that require attention when you are free")
        else:
            print(f"'{task}' is a low priority task. Consider completing it when you have a free time")
  