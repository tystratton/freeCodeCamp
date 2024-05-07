def add_time(start, duration, day=""):
    week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    start = start.split()
    # Get hour and minute from start and conver to int
    am_pm = start[1]
    print(am_pm)
    split = start[0].split(":")
    hour = int(split[0])
    minute = int(split[1])
    
    
    duration = duration.split()
    split = duration[0].split(":")
    hoursToAdd = int(split[0])
    # if minutes starts with a 0
    if split[1][0] == "0":
        minutesToAdd = int(split[1][1])
    else:
        minutesToAdd = int(split[1])
    leftoverHours = hoursToAdd % 24 # leftover hours - 10
    days = hoursToAdd // 24 # 466 - 19 days
    print("leftoverhours: " + str(leftoverHours))
    print("minute: " + str(minute))
    print("minutestoadd: " + str(minutesToAdd))
    print("days after: " + str(days))
    # if AM/PM changes
    if minute + minutesToAdd > 0:
        minute = (minute + minutesToAdd) - 60
        hour = hour + 1
    else:
        minute = minute + minutesToAdd
    if len(str(minute)) == 1:
        minute = "0" + str(minute)

    #finding whether or not to change AM/PM
    findingout = hour + leftoverHours + (minutesToAdd/60)
    print(findingout)
    if hour + leftoverHours + (minutesToAdd/60) > 12:
        hour = (hour + leftoverHours) % 12
        print("FINDINGOUT2: " + str(hour))
        if hour == 0 and "am_pm" == "AM":
            am_pm == "PM"
            hour = 12
        elif hour == 0 and "am_pm" == "PM":
            am_pm == "AM"
            hour = 12
        elif "am_pm" == "AM":
            am_pm == "PM"
        elif "am_pm" == "PM":
            am_pm == "AM"

    print(hour)
    else:
        hour = hour + leftoverHours

    
    if day:
        day = day.lower()
        index = 0
        while index < len(week):
            if day == week[index]:
                dayIndex = index
            index += 1
        dayIndex = (dayIndex + days) % 7
        day = week[dayIndex].capitalize()
        if days == 1:
            new_time = str(hour) + ":" + str(minute) + " " + str(am_pm) + ", " + day + " " + "(next day)"
        elif days > 1:
            new_time = str(hour) + ":" + str(minute) + " " + str(am_pm) + ", " + day + " " + "(" + str(days) + " days later)"
        else:
            new_time = str(hour) + ":" + str(minute) + " " + str(am_pm) + ", " + day

    else:
        if days == 1:
            new_time = str(hour) + ":" + str(minute) + " " + str(am_pm) + " " + "(next day)"
        elif days > 1:
            new_time = str(hour) + ":" + str(minute) + " " + str(am_pm) + " " + "(" + str(days) + " days later)"
        else:
            new_time = str(hour) + ":" + str(minute) + " " + str(am_pm)
    return new_time

print((f'\n{add_time('11:43 PM', '24:20', 'tueSday')}'))