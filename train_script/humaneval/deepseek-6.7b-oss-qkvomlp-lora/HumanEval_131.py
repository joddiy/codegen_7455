def digits(n):
    product = 1
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
        n //= 10
    return product if product != 1 else 0