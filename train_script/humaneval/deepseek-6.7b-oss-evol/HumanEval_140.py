def fix_spaces(text):
    return text.replace("  ", "-").replace(" ", "_")

print(fix_spaces("Example")) # "Example"
print(fix_spaces("Example 1")) # "Example_1"
print(fix_spaces(" Example 2")) # "_Example_2"
print(fix_spaces(" Example   3")) # "_Example-3"