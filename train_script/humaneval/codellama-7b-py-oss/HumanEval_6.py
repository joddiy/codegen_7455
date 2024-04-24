from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    max_depth = 0
    result = []
    stack = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
            max_depth = max(max_depth, len(stack))
        elif char == ')':
            stack.pop()
            result.append(max_depth)
    return result