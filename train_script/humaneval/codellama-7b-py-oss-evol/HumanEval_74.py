def total_match(lst1, lst2):
    # Calculate the total number of characters in each list
    total_chars_lst1 = sum(len(word) for word in lst1)
    total_chars_lst2 = sum(len(word) for word in lst2)

    # If the total number of characters in lst1 is less than lst2, return lst1
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    # If the total number of characters in lst2 is less than lst1, return lst2
    elif total_chars_lst2 < total_chars_lst1:
        return lst2
    # If the total number of characters in both lists are equal, return lst1
    else:
        return lst1