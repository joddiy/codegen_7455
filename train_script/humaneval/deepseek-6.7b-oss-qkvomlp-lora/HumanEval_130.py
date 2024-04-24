def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    elif n == 2:
        return [0, 1, 1]
    else:
        trib = [0, 1, 1]
        for i in range(3, n+1):
            trib.append(trib[i-1] + trib[i-2] + trib[i-3])
        return trib