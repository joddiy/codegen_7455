def solve(N):
    binary_str = bin(N)[2:]  # Convert the integer to binary string
    total_sum = sum(int(digit) for digit in binary_str)  # Calculate the sum of digits in binary
    return binary_str  # Return the binary string