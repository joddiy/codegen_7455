def median(l: list):
    l.sort()
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))