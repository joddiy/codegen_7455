def match_parens(lst):
    s1, s2 = lst[0], lst[1]
    return 'Yes' if (s1 + s2).count('(') - (s1 + s2).count(')') == 0 else 'No'