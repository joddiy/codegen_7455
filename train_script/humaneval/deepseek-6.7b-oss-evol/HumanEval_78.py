def hex_key(num):
    hex_digits = '2357BDF'
    count = 0
    for digit in num:
        if digit in hex_digits:
            count += 1
    return count