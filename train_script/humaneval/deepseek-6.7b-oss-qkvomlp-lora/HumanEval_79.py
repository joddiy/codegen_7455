def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary using built-in bin function
    binary = 'db' + binary + 'db'  # Add extra characters 'db' at the beginning and at the end
    return binary