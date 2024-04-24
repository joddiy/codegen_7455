def correct_bracketing(brackets: str):
    stack = []
    bracket_map = {"<": ">", ">": "<"}
    for b in brackets:
        if b in bracket_map:
            stack.append(b)
        elif stack and stack[-1] == bracket_map[b]:
            stack.pop()
        else:
            return False
    return len(stack) == 0