def right_angle_triangle(a, b, c):
    # Sort the sides to ensure c is the longest side
    sides = sorted([a, b, c])
    # Check if the longest side is equal to the sum of the other two sides
    return sides[-1] == sides[0] + sides[1]

print(right_angle_triangle(3, 4, 5)) # True
print(right_angle_triangle(1, 2, 3)) # False