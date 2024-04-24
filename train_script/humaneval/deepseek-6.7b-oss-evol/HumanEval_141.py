import re

def file_name_check(file_name):
    # Check if there are more than three digits in the file name
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'

    # Check if there is exactly one dot in the file name
    if file_name.count('.') != 1:
        return 'No'

    # Split the file name into the substring before and after the dot
    before_dot, after_dot = file_name.split('.')

    # Check if the substring before the dot starts with a letter and is not empty
    if not before_dot or not before_dot[0].isalpha():
        return 'No'

    # Check if the substring after the dot is one of the allowed extensions
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    # If all checks pass, return 'Yes'
    return 'Yes'

# Test cases
print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No'
print(file_name_check("example123.txt")) # => 'No'
print(file_name_check("example..txt")) # => 'No'
print(file_name_check("example.exe")) # => 'Yes'