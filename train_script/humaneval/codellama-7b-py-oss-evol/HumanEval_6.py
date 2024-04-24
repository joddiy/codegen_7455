from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def count_nested_parens(s: str) -> int:
        count = 0
        max_count = 0
        for char in s:
            if char == '(':
                count += 1
                max_count = max(max_count, count)
            elif char == ')':
                count -= 1
        return max_count

    return [count_nested_parens(s) for s in paren_string.split()]

print(parse_nested_parens('(()()) ((())) () ((())()())'))