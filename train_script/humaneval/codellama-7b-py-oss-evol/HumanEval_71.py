def triangle_area(a, b, c):
    # Check if the sides can form a triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate the area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        # Round the area to 2 decimal points
        area = round(area, 2)
        return area
    else:
        return -1

# Test the function
print(triangle_area(3, 4, 5))  # Expected output: 6.0
print(triangle_area(1, 2, 10))  # Expected output: -1