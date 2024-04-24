def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_sequence = [0, 0, 1]
        for i in range(3, n+1):
            fibfib_sequence.append(fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3])
        return fibfib_sequence[n]

print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24