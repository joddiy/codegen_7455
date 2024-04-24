def reverse_delete(s, c):
    # Delete all characters in s that are equal to any character in c
    s = ''.join(ch for ch in s if ch not in c)

    # Check if the result string is palindrome
    is_palindrome = s == s[::-1]

    return s, is_palindrome

# Test cases
print(reverse_delete("abcde", "ae"))  # ('bcd', False)
print(reverse_delete("abcdef", "b"))  # ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # ('cdedc', True)