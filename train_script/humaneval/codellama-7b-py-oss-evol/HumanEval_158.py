def find_max(words):
    max_unique_count = 0
    max_word = ""
    for word in words:
        unique_count = len(set(word))
        if unique_count > max_unique_count:
            max_unique_count = unique_count
            max_word = word
        elif unique_count == max_unique_count:
            max_word = min(max_word, word)
    return max_word

print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb" ,"cc"]))  # Output: "aaaaaaa"