print("test")

day = "Monday"

# Match the day to predefined patterns
match day:
    case "Saturday" | "Sunday":
        print(f"{day} is a weekend.")  # Match weekends
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{day} is a weekday.")  # Match weekdays
    case _:
        print("That's not a valid day of the week.")  # Default case