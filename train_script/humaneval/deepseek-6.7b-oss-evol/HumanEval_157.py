def right_angle_triangle(a, b, c):
    # Check if the triangle is valid
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    # Check if the triangle is a right-angled triangle
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False

# Test cases
print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False