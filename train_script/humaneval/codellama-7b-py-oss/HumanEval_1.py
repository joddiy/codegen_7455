from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    result = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                result.append('()')
            else:
                stack.pop()
                result.append(''.join(stack + [char]))
    return result