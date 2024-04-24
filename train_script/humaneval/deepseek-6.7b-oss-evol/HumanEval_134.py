def check_if_last_char_is_a_letter(txt):
    if txt:
        last_char = txt[-1]
        if last_char.isalpha():
            if txt.count(last_char) == 1:
                if txt.rindex(last_char) == len(txt) - 1:
                    return True
    return False

print(check_if_last_char_is_a_letter("apple pie"))  # ➞ False
print(check_if_last_char_is_a_letter("apple pi e"))  # ➞ True
print(check_if_last_char_is_a_letter("apple pi e "))  # ➞ False
print(check_if_last_char_is_a_letter(""))  # ➞ False