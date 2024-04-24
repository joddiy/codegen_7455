def order_by_points(nums):
    # Create a list of tuples containing the sum of digits and the original number
    nums_with_points = [(sum(int(digit) for digit in str(abs(num))), num) for num in nums]
    
    # Sort the list of tuples based on the sum of digits and original number
    sorted_nums = sorted(nums_with_points)
    
    # Extract the original numbers from the sorted list of tuples
    result = [num for _, num in sorted_nums]
    
    return result