def search(lst):
    from collections import Counter
    counter = Counter(lst)
    for num in sorted(counter.keys(), reverse=True):
        if num > 0 and counter[num] >= num:
            return num
    return -1