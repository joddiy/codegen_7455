import re

def file_name_check(file_name):
    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Split the file name into name and extension
    name, extension = file_name.split('.')

    # Check if the name starts with a letter from the latin alphapet
    if not name[0].isalpha():
        return 'No'

    # Check if the file name contains at most three digits
    if len(re.findall(r'\d', name)) > 3:
        return 'No'

    # Check if the extension is one of the allowed types
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'