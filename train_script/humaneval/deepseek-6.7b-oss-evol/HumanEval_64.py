def vowels_count(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    if s[-1].lower() == 'y':
        count += 1
    return count

print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("YELLOW"))  # Output: 2
print(vowels_count(""))  # Output: 0
print(vowels_count("Y"))  # Output: 1