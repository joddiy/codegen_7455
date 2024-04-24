def match_parens(lst):
    open_count = 0
    close_count = 0
    for char in lst[0]:
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
    for char in lst[1]:
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
    if open_count == close_count:
        return 'Yes'
    else:
        return 'No'