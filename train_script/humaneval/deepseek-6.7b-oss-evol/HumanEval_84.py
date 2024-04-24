def solve(N):
    # Convert the integer to binary
    binary_num = bin(N)[2:]
    # Calculate the sum of the digits
    sum_of_digits = sum(int(digit) for digit in binary_num)
    # Convert the sum to binary
    binary_sum = bin(sum_of_digits)[2:]
    return binary_sum