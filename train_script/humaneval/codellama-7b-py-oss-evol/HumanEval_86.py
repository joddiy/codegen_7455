def anti_shuffle(s):
    words = s.split(' ')
    ordered_words = []
    for word in words:
        ordered_chars = sorted(word)
        ordered_words.append(''.join(ordered_chars))
    return ' '.join(ordered_words)

print(anti_shuffle('Hi'))  # returns 'Hi'
print(anti_shuffle('hello'))  # returns 'ehllo'
print(anti_shuffle('Hello World!!!'))  # returns 'Hello !!!Wdlor'