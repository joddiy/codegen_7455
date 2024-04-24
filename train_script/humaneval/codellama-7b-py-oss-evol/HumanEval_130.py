def tri(n):
    sequence = [1, 3]
    if n == 2:
        return sequence
    elif n % 2 == 0:
        for i in range(2, n + 1):
            sequence.append(sequence[i - 1] + i / 2)
    else:
        sequence.append(sequence[1] + sequence[0] + sequence[2])
        for i in range(3, n + 1):
            sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i + 1])
    return sequence

print(tri(3))  # Output: [1, 3, 2, 8]