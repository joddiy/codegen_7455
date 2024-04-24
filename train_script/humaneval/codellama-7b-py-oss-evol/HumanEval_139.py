def special_factorial(n):
    if n < 0:
        return "Error: n must be a positive integer"
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        return factorial

print(special_factorial(4))