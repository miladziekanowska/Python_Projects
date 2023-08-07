def add_time(start, duration, day_of_the_week=None):
    # local variables
    [beggining, half_of_day] = start.split()
    [hour, minutes] = beggining.split(sep=":")
    hour = int(hour)
    minutes = int(minutes)
    [d_hours, d_minutes] = duration.split(sep=":")
    d_hours = int(d_hours)
    d_minutes = int(d_minutes)

    #calculating how many days it takes (if it does take days)
    d_days = d_hours // 24
    d_hours = d_hours % 24

    #calculating new minutes
    new_minutes = minutes + d_minutes

    if new_minutes == 60:
        new_minutes = 0
        d_hours += 1
    elif new_minutes > 60:
        new_minutes = new_minutes - 60
        d_hours += 1

    if new_minutes < 10:
        new_minutes = f"0{new_minutes}"

    #calculating new hours
    new_hour = hour + d_hours

    if half_of_day == "AM":
        if new_hour == 12:
            half_of_day = "PM"
        elif new_hour > 12:
            new_hour = new_hour - 12
            half_of_day = "PM"
    elif half_of_day == "PM":
        if new_hour == 12:
            half_of_day = "AM"
            d_days += 1
        elif new_hour > 12:
            new_hour = new_hour - 12
            half_of_day = "AM"
            d_days += 1

    # preparing the day_of_the_week variable, if inserted
    days_of_week = ["Monday", 
                    "Tuesday", 
                    "Wednesday", 
                    "Thursday", 
                    "Friday", 
                    "Saturday",
                    "Sunday"]

    if day_of_the_week is not None:
        day_of_the_week = day_of_the_week.capitalize()
        if day_of_the_week in days_of_week:
            index = days_of_week.index(day_of_the_week)
            new_index = (index + d_days) % len(days_of_week)
            new_day_name = days_of_week[new_index]

    # preparing the next or x days later tag
    if d_days == 1:
        days = "(next day)"
    elif d_days > 1:
        days = f"({d_days} days later)"
        
        
    # assembling the new_time 
    if day_of_the_week is not None:
        if d_days >= 1:
            new_time = f"{new_hour}:{new_minutes} {half_of_day}, {new_day_name} {days}"
        else:
            new_time = f"{new_hour}:{new_minutes} {half_of_day}, {new_day_name}"
    else:
        if d_days >= 1:
            new_time = f"{new_hour}:{new_minutes} {half_of_day} {days}"
        else:
            new_time = f"{new_hour}:{new_minutes} {half_of_day}"

    return new_time
