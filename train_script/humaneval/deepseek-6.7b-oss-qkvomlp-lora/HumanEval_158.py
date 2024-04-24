def find_max(words):
    max_unique_chars = max(len(set(word)) for word in words)
    max_words = [word for word in words if len(set(word)) == max_unique_chars]
    return min(max_words) if max_words else ""