import hashlib

def string_to_md5(text):
    if text == "":
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()

print(string_to_md5('Hello world'))  # Output: '3e25960a79dbc69b674cd4ec67a72c62'