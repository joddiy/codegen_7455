from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map the string numbers to their corresponding integer values
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # Split the input string into a list of numbers
    num_list = numbers.split()

    # Convert each number in the list to its corresponding integer value
    num_list = [num_dict[num] for num in num_list]

    # Sort the list of numbers
    num_list.sort()

    # Convert each number in the list back to its corresponding string value
    num_list = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in num_list]

    # Join the list of numbers back into a string
    sorted_numbers = ' '.join(num_list)

    return sorted_numbers

print(sort_numbers('three one five'))