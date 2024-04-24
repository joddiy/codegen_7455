def correct_bracketing(brackets: str):
    stack = []
    opening_brackets = set(["(", "[", "{"])
    closing_brackets = set([")", "]", "}"])
    bracket_pairs = {")": "(", "]": "[", "}": "{"}

    for char in brackets:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return not stack