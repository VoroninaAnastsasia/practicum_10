def seconds_from_start(datetime_str):
    """Returns the number of seconds since the beginning of the year."""

    date_part, time_part = datetime_str.split()
    month, day, year = map(int, date_part.split('/'))
    hour, minute, second = map(int, time_part.split(':'))

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29

    days = 0
    for i in range(month - 1):
        days += days_in_month[i]
    days += day - 1
    
    return days * 86400 + hour * 3600 + minute * 60 + second

print(seconds_from_start("01/02/2023 00:00:00"))
