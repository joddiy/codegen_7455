def count_nums(arr):
    count = 0
    for num in arr:
        if sum(int(digit) for digit in str(abs(num))) > 0:
            count += 1
    return count

print(count_nums([])) # 0
print(count_nums([-1, 11, -11])) # 1
print(count_nums([1, 1, 2])) # 3