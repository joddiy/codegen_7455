def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    words = s.split()  # Split the input string into words
    ordered_words = []  # Initialize an empty list to store ordered words

    for word in words:
        ordered_word = ''.join(sorted(word))  # Sort each word based on ascii value
        ordered_words.append(ordered_word)  # Add the ordered word to the list

    return ' '.join(ordered_words)  # Join the ordered words with spaces and return the result