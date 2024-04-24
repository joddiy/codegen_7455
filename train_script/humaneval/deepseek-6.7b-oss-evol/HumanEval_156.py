def int_to_mini_roman(number):
    # Define the mapping of integers to roman numerals
    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix',
        10: 'x', 40: 'xl', 50: 'l', 90: 'xc',
        100: 'c', 400: 'cd', 500: 'd', 900: 'cm',
        1000: 'm'
    }

    # Initialize an empty string to store the roman numeral
    roman_numeral = ''

    # Iterate over the keys in descending order
    for value in sorted(roman_numerals.keys(), reverse=True):
        # While the number is greater than or equal to the current value
        while number >= value:
            # Add the corresponding roman numeral to the result
            roman_numeral += roman_numerals[value]
            # Subtract the value from the number
            number -= value

    # Return the roman numeral
    return roman_numeral