def even_odd_count(num):
    # convert the number to string
    num_str = str(abs(num))
    # initialize counters
    even_count = 0
    odd_count = 0
    # iterate over each digit
    for digit in num_str:
        # check if the digit is even or odd
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    # return the counts as a tuple
    return (even_count, odd_count)

# test the function
print(even_odd_count(-12))  # should return (1, 1)
print(even_odd_count(123))  # should return (1, 2)