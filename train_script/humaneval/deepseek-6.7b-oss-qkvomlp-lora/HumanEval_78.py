def hex_key(num):
    primes = [2, 3, 5, 7, 11, 13]
    count = 0
    for char in num:
        if char.isdigit():
            if int(char) in primes:
                count += 1
        elif char.upper() in ['A', 'B', 'C', 'D', 'E', 'F']:
            if int(char, 16) in primes:
                count += 1
    return count