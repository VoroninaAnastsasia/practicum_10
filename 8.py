def convert_datetime(datetime_str):
    """The function converts date and time from the format
    "MM/DD/YYYY HR:MIN:SEC" to the format "DD.MM.YY HR:MIN:SEC"
    with a 12-hour time format"""
    
    try:
        date_part, time_part = datetime_str.split()
    except:
        print("Ошибка: Неверный формат строки")
        return
    
    try:
        month, day, year = map(int, date_part.split('/'))
    except:
        print("Ошибка: Неверный формат даты")
        return

    try:
        hour, minute, second = map(int, time_part.split(':'))
    except:
        print("Ошибка: Неверный формат времени")
        return
    
    if not (1 <= month <= 12):
        print("Ошибка: Некорректный месяц (1-12)")
        return
    
    if not (1 <= day <= 31):
        print("Ошибка: Некорректный день (1-31)")
        return
    
    if not (0 <= hour <= 23):
        print("Ошибка: Некорректный час (0-23)")
        return
    
    if not (0 <= minute <= 59):
        print("Ошибка: Некорректные минуты (0-59)")
        return
    
    if not (0 <= second <= 59):
        print("Ошибка: Некорректные секунды (0-59)")
        return

    year_short = year % 100
    
    if hour == 0:
        hour_12 = 12
        period = "AM"
    elif hour < 12:
        hour_12 = hour
        period = "AM"
    elif hour == 12:
        hour_12 = 12
        period = "PM"
    else:
        hour_12 = hour - 12
        period = "PM"

    print(f"{day:02d}.{month:02d}.{year_short:02d} {hour_12:02d}:{minute:02d}:{second:02d} {period}")

convert_datetime("12/25/2023 14:30:45")
