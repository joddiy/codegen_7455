def odd_count(lst):
    result = []
    for i in range(len(lst)):
        odd_count = 0
        for char in lst[i]:
            if int(char) % 2 != 0:
                odd_count += 1
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(odd_count, odd_count, i+1, len(lst)))
    return result