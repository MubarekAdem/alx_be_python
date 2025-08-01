# daily_reminder.py

def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority entered.")
            return

    if time_bound == "yes":
        print(
            f"Reminder: {base_message} that requires immediate attention today!")
    else:
        print(
            f"Reminder: Note: {base_message}. Consider completing it when you have free time.")


if __name__ == "__main__":
    main()
