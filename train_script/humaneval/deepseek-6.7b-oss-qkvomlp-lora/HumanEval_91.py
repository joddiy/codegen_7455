def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'
    """
    sentences = S.split('.') + S.split('?') + S.split('\n')
    count = 0
    for sentence in sentences:
        if sentence.startswith('I'):
            count += 1
    return count