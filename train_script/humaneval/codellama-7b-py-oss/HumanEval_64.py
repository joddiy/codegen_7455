def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = set('aeiouAEIOU')
    if s[-1] == 'y' and s[-2] not in vowels:
        return sum(1 for char in s if char in vowels) + 1
    else:
        return sum(1 for char in s if char in vowels)