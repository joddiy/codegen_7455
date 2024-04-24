def valid_date(date):
    try:
        month, day, year = map(int, date.split('-'))
        if month in [1, 3, 5, 7, 8, 10, 12] and not (1 <= day <= 31):
            return False
        elif month in [4, 6, 9, 11] and not (1 <= day <= 30):
            return False
        elif month == 2 and not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) and not (1 <= day <= 29)):
            return False
        elif not (1 <= month <= 12):
            return False
        return True
    except ValueError:
        return False