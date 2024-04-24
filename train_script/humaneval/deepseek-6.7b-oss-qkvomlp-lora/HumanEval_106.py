def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            result.append(factorial)
        else:
            sum_of_numbers = sum(range(1, i+1))
            result.append(sum_of_numbers)
    return result