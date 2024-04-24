def encode(message):
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded_char = chr((ord(char.lower()) - ord('a') + 2) % 26 + ord('a'))
                encoded_message += encoded_char.upper() if char.isupper() else encoded_char
            else:
                encoded_message += char.upper() if char.islower() else char.lower()
        else:
            encoded_message += char
    return encoded_message

print(encode('test'))
print(encode('This is a message'))