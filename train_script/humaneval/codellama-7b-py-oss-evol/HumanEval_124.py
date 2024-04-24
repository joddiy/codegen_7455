def valid_date(date):
    import re
    # Check if the date is in the correct format
    if not re.match(r'^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})$', date):
        return False
    # Extract the month, day, and year from the date
    month, day, year = map(int, date.split('-'))
    # Check if the month is valid
    if month < 1 or month > 12:
        return False
    # Check if the day is valid
    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return False
    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    if month == 2 and (day < 1 or day > 29):
        # Check if the year is a leap year
        if year % 4 != 0:
            return False
        if year % 100 != 0:
            return True
        if year % 400 != 0:
            return False
        return True
    return True