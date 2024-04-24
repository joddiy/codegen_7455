def rounded_avg(n, m):
    if n > m:
        return -1
    else:
        average = round((n + m) / 2)
        binary_str = bin(average)[2:]  # Convert the average to binary
        return binary_str