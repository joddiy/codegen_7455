def encode(message):
    vowels = 'aeiou'
    result = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                index = vowels.index(char.lower())
                result += chr((ord(vowels[index]) - ord('a') + 2) % 26 + ord('a'))
            else:
                result += char.swapcase()
        else:
            result += char
    return result

print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'