def rounded_avg(n, m):
    if n > m:
        return -1
    else:
        avg = (n + m) / 2
        rounded_avg = int(avg)
        binary_avg = bin(rounded_avg)
        return binary_avg