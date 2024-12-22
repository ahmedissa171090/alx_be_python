# daily_reminder.py

def main():
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Generate reminder based on priority
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            return

    # Modify reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += " Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound. Please enter yes or no.")
        return

    # Print the final reminder
    print(f"\nReminder: {reminder}")

if __name__ == "__main__":
    main()
