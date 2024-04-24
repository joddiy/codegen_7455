def vowels_count(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    if s[-1].lower() == 'y':
        count += 1
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("Hello"))  # Output: 2
print(vowels_count("Yo"))  # Output: 1
print(vowels_count("Y"))  # Output: 1
print(vowels_count(""))  # Output: 0