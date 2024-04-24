def file_name_check(file_name):
    # Check if there are more than three digits in the file name
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'

    # Check if there is exactly one dot in the file name
    if file_name.count('.') != 1:
        return 'No'

    # Check if the substring before the dot starts with a letter and is not empty
    if not file_name.split('.')[0] or not file_name.split('.')[0][0].isalpha():
        return 'No'

    # Check if the substring after the dot is one of the allowed extensions
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

# Test the function
print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No'