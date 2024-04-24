def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    last_char = txt[-1]
    if last_char.isalpha() and txt[-2] != ' ':
        return True
    else:
        return False