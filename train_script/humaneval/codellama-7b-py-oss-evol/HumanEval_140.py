def fix_spaces(text):
    result = ''
    space_count = 0
    for char in text:
        if char == ' ':
            space_count += 1
            if space_count > 2:
                result += '-'
                space_count = 0
            else:
                result += '_'
        else:
            result += char
    return result

print(fix_spaces("Example")) # "Example"
print(fix_spaces("Example 1")) # "Example_1"
print(fix_spaces(" Example 2")) # "_Example_2"
print(fix_spaces(" Example   3")) # "_Example-3"