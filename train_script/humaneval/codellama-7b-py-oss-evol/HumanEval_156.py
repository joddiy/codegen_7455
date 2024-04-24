def int_to_mini_roman(number):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    roman_numeral = ''
    for i in range(len(values)):
        count = number // values[i]
        roman_numeral += numerals[i] * count
        number -= values[i] * count
    return roman_numeral