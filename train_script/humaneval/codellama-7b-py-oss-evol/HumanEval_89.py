def encrypt(s):
    result = ""
    for v in s:
        if v.isalpha():
            shift = 2 * 2
            ascii_offset = ord('a') if v.islower() else ord('A')
            result += chr((ord(v) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += v
    return result

print(encrypt('hi'))  # returns 'lm'
print(encrypt('asdfghjkl'))  # returns 'ewhjklnop'
print(encrypt('gf'))  # returns 'kj'
print(encrypt('et'))  # returns 'ix'