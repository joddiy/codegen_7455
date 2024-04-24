def is_bored(S):
    # Split the string into sentences
    sentences = S.split('.') + S.split('!') + S.split('?')
    # Initialize the count of boredoms
    boredom_count = 0
    # Iterate over the sentences
    for sentence in sentences:
        # If the sentence starts with "I", increment the count
        if sentence.strip().startswith("I"):
            boredom_count += 1
    # Return the count of boredoms
    return boredom_count