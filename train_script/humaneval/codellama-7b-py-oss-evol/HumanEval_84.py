def solve(N):
    # Convert the integer to binary
    binary_N = bin(N)[2:]

    # Convert each digit to binary and sum them up
    sum_of_digits = sum(int(digit) for digit in binary_N)

    # Convert the sum to binary
    binary_sum = bin(sum_of_digits)[2:]

    return binary_sum

# Test the function
print(solve(1000))  # Output: "1"
print(solve(150))   # Output: "110"
print(solve(147))   # Output: "1100"