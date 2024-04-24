def histogram(test):
    # Split the string into a list of characters
    chars = test.split()

    # Create a dictionary to store the count of each character
    count_dict = {}

    # Iterate over each character in the list
    for char in chars:
        # If the character is already in the dictionary, increment its count
        if char in count_dict:
            count_dict[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            count_dict[char] = 1

    # Find the maximum count
    max_count = max(count_dict.values()) if count_dict else 0

    # Create a new dictionary to store the characters with the maximum count
    result_dict = {char: count for char, count in count_dict.items() if count == max_count}

    return result_dict