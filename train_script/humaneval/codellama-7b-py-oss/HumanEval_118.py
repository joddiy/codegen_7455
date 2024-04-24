def get_closest_vowel(word):
    vowels = "AEIOU"
    for i in range(len(word) - 2, -1, -1):
        if word[i] in vowels and word[i + 1] not in vowels and word[i + 2] in vowels:
            return word[i + 1]
    return ""