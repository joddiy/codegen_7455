def is_bored(S):
    """
    Count the number of boredoms in the given string.
    """
    boredoms = 0
    sentences = S.split('. ')
    for sentence in sentences:
        words = sentence.split()
        if words and words[0] == 'I':
            boredoms += 1
    return boredoms