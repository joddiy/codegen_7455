def is_bored(S):
    sentences = S.split('. ')
    count = 0
    for sentence in sentences:
        words = sentence.split(' ')
        if words[0] == 'I':
            count += 1
    return count