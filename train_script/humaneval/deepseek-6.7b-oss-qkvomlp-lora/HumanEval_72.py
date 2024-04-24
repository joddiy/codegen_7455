def will_it_fly(q, w):
    if sum(q) <= w and q == q[::-1]:
        return True
    else:
        return False