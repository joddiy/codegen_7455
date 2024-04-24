def special_factorial(n):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    result = 1
    for i in range(n, 0, -1):
        result *= factorial(i)
    return result