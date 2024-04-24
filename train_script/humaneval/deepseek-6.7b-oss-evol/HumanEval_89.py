def encrypt(s):
    result = ""
    for i in s:
        if i.isalpha():
            shift = 2
            char = i.lower()
            ascii_val = ord(char)
            new_ascii_val = ascii_val + shift
            if new_ascii_val > ord('z'):
                new_ascii_val -= 26
            result += chr(new_ascii_val)
        else:
            result += i
    return result