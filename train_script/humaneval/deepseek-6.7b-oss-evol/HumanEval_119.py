def match_parens(lst):
    s = ''.join(lst)
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 'No'
    return 'Yes' if not stack else 'No'

print(match_parens(['()(', ')']))  # 'Yes'
print(match_parens([')', ')']))  # 'No'