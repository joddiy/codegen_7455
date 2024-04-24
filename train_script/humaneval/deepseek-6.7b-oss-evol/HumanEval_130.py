def tri(n):
    tribonacci = [1, 3, 2]
    if n < 3:
        return tribonacci[:n+1]
    else:
        for i in range(3, n+1):
            if i % 2 == 0:
                tribonacci.append(1 + (i / 2))
            else:
                tribonacci.append(tribonacci[i-1] + tribonacci[i-2] + tribonacci[i-3])
        return tribonacci