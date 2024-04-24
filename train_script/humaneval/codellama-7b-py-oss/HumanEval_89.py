def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            shift = 26 - (ord(char) - 97) * 2  # Rotate the alphabet by 2 places
            encrypted_string += chr(97 + shift) if char.islower() else chr(65 + shift)
        else:
            encrypted_string += char
    return encrypted_string