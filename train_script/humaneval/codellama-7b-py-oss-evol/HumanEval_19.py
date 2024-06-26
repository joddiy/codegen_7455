from typing import List

def sort_numbers(numbers: str) -> str:
    # Convert the string into a list of words
    words = numbers.split()

    # Convert each word into a number
    numbers = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    # Sort the list of words by their corresponding numbers
    words.sort(key=lambda word: numbers[word])

    # Convert the list of words back into a string
    return ' '.join(words)

print(sort_numbers('three one five'))  # Output: 'one three five'