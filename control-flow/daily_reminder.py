# daily_reminder.py

def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority entered.")
            return

    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message = "Note: " + message + ". Consider completing it when you have free time."

    print("\nReminder:", message)


if __name__ == "__main__":
    main()
