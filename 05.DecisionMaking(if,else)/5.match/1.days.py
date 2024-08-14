def get_day_name(day):
    match day:
        case "Monday":
            return "Today is Monday"
        case "Tuesday":
            return "Today is Tuesday"
        case "Wednesday":
            return "Today is Wednesday"
        case "Thursday":
            return "Today is Thursday"
        case "Friday":
            return "Today is Friday"
        case _:
            return "It's a weekend day"

day = "Wednesday"
print(get_day_name(day))
