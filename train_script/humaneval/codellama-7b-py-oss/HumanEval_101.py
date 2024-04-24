def words_string(s):
    """
    Splits the string into words and returns an array of the words.

    Args:
    s: A string of words separated by commas or spaces.

    Returns:
    A list of words from the input string.
    """
    # Split the string into words using either commas or spaces as delimiters
    words = s.split(', ')
    if ',' in s and ' ' in s:
        words = s.split(', ')
    elif ',' in s:
        words = s.split(',')
    elif ' ' in s:
        words = s.split()
    return words