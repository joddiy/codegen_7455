def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            str_num = str(abs(num))
            if int(str_num[0]) % 2 == 1 and int(str_num[-1]) % 2 == 1:
                count += 1
    return count