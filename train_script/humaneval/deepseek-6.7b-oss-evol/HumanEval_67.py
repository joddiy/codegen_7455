def fruit_distribution(s,n):
    # split the string to get the number of apples and oranges
    apples, oranges = map(int, s.split()[::2])
    # calculate the number of mangoes
    mangoes = n - apples - oranges
    return mangoes