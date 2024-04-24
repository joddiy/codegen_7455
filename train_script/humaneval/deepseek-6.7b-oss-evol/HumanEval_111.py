def histogram(test):
    # Create a dictionary to store the count of each letter
    letter_count = {}

    # Split the string into a list of words
    words = test.split()

    # Iterate over each word
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in letter_count:
            letter_count[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            letter_count[word] = 1

    # Find the maximum count
    max_count = max(letter_count.values()) if letter_count else 0

    # Create a new dictionary to store the letters with the maximum count
    max_letters = {k: v for k, v in letter_count.items() if v == max_count}

    return max_letters