def hex_key(num):
    hex_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'}
    primes = {2, 3, 5, 7, 11, 13}
    count = 0
    for digit in num:
        if digit in hex_digits and int(digit, 16) in primes:
            count += 1
    return count