def largest_smallest_integers(lst):
    neg_nums = [num for num in lst if num < 0]
    pos_nums = [num for num in lst if num > 0]

    if neg_nums:
        largest_neg = max(neg_nums)
    else:
        largest_neg = None

    if pos_nums:
        smallest_pos = min(pos_nums)
    else:
        smallest_pos = None

    return (largest_neg, smallest_pos)