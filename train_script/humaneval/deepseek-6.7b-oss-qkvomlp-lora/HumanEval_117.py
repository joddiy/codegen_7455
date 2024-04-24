def select_words(s, n):
    words = s.split()
    selected_words = []
    for word in words:
        consonants = [char for char in word if char.lower() not in 'aeiou']
        if len(consonants) == n:
            selected_words.append(word)
    return selected_words