def cycpattern_check(a, b):
    if b in a:
        return True
    for i in range(len(b)):
        if b in a + a[i:] + a[:i]:
            return True
    return False