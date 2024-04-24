from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    strings.sort(key=len, reverse=True)
    return strings[0]