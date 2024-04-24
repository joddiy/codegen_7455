def odd_count(lst):
    result = []
    for i, string in enumerate(lst, start=1):
        odd_count = sum(int(digit) % 2 for digit in string)
        result.append("the number of odd elements in the string {} of the input.".format(odd_count))
    return result

print(odd_count(['1234567']))
print(odd_count(['3',"11111111"]))