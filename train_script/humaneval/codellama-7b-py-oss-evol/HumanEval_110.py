def exchange(lst1, lst2):
    # Initialize counters for even and odd numbers in lst1 and lst2
    count_lst1_even = count_lst1_odd = count_lst2_even = count_lst2_odd = 0

    # Count the number of even and odd numbers in lst1 and lst2
    for num in lst1:
        if num % 2 == 0:
            count_lst1_even += 1
        else:
            count_lst1_odd += 1

    for num in lst2:
        if num % 2 == 0:
            count_lst2_even += 1
        else:
            count_lst2_odd += 1

    # If there are more odd numbers in lst1 than in lst2, return "NO"
    if count_lst1_odd > count_lst2_odd:
        return "NO"

    # If there are more even numbers in lst2 than in lst1, return "YES"
    if count_lst2_even > count_lst1_even:
        return "YES"

    # If there are the same number of even and odd numbers in both lists, return "YES"
    return "YES"