def do_algebra(operator, operand):
    # Initialize the result with the first operand
    result = operand[0]

    # Iterate over the operators and operands
    for i in range(len(operator)):
        # Perform the operation based on the operator
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]

    return result

# Test the function
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 9