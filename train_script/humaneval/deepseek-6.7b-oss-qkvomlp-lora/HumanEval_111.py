def histogram(test):
    # Split the input string into a list of lowercase letters
    letters = test.lower().split()
    
    # Create a dictionary to store the count of each letter
    letter_count = {}
    
    # Iterate through the list of letters
    for letter in letters:
        # If the letter is already in the dictionary, increment its count
        if letter in letter_count:
            letter_count[letter] += 1
        # Otherwise, add the letter to the dictionary with a count of 1
        else:
            letter_count[letter] = 1
    
    # Find the letter with the most repetition
    max_count = max(letter_count.values())
    
    # Create a dictionary to store the letters with the most repetition
    result = {}
    
    # Iterate through the letter count dictionary
    for letter, count in letter_count.items():
        # If the count matches the maximum count, add the letter to the result dictionary
        if count == max_count:
            result[letter] = count
    
    return result

if __name__ == '__main__':
    print(histogram('a b a c a b'))
