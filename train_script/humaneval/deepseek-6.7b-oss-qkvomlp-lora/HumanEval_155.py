def even_odd_count(num):
    num = abs(num)
    even_count = 0
    odd_count = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10
    return (even_count, odd_count)