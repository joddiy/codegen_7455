def sort_even(l: list):
    even_indicies = [l[i] for i in range(0, len(l), 2)]
    even_indicies.sort()
    result = []
    even_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_indicies[even_index])
            even_index += 1
        else:
            result.append(l[i])
    return result

print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))