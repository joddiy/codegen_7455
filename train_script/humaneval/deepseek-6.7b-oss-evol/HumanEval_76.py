def is_simple_power(x, n):
    if x == 1:
        return True
    elif x < n:
        return False
    else:
        while x % n == 0:
            x /= n
        return x == 1