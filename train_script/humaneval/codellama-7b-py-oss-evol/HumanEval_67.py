def fruit_distribution(s,n):
    # Split the string into two parts: the number of apples and oranges, and the rest of the string
    parts = s.split("apples and ")
    # Convert the number of apples and oranges to integers
    num_apples = int(parts[0])
    num_oranges = int(parts[1])
    # Return the number of mango fruits
    return n - num_apples - num_oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # -> 8
print(fruit_distribution("0 apples and 1 oranges",3)) # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # -> 95
print(fruit_distribution("100 apples and 1 oranges",120)) # -> 19