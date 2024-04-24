def order_by_points(nums):
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))
    return sorted_nums