def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        area = 0.5 * (a + b + c) * (a - b) * (a - c) * (b - c)
        return round(area ** 0.5, 2)
    else:
        return -1