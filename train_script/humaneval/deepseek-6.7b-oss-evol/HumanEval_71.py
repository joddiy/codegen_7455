import math

def triangle_area(a, b, c):
    # Check if the sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate the area using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        # Return the area rounded to 2 decimal points
        return round(area, 2)
    else:
        # Return -1 if the sides do not form a valid triangle
        return -1

# Test cases
print(triangle_area(3, 4, 5))  # Should print 6.0
print(triangle_area(1, 2, 10))  # Should print -1