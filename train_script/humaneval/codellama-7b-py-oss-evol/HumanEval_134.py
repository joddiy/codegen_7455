def check_if_last_char_is_a_letter(txt):
    if txt == "":
        return False
    last_char = txt[-1]
    if last_char.isalpha():
        return not last_char.isalnum()
    else:
        return False

print(check_if_last_char_is_a_letter("apple pie"))  # ➞ False
print(check_if_last_char_is_a_letter("apple pi e"))  # ➞ True
print(check_if_last_char_is_a_letter("apple pi e "))  # ➞ False
print(check_if_last_char_is_a_letter(""))  # ➞ False