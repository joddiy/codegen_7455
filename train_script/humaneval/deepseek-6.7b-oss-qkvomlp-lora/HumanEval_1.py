from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    start = 0
    count = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            count += 1
        elif paren_string[i] == ')':
            count -= 1
        if count == 0:
            groups.append(paren_string[start:i+1])
            start = i + 1
    return groups