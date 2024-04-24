def total_match(lst1, lst2):
    if len(lst1) == 0 or len(lst2) == 0:
        return []

    total_chars_lst1 = sum(len(s) for s in lst1)
    total_chars_lst2 = sum(len(s) for s in lst2)

    if total_chars_lst1 == total_chars_lst2:
        return lst1
    elif total_chars_lst1 < total_chars_lst2:
        return lst1
    else:
        return lst2