def smallest_change(arr):
    n = len(arr)
    # Create a frequency dictionary
    freq = {}
    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    # Count the frequency of elements in the first half of the array
    first_half = n // 2
    count = 0
    for i in range(first_half):
        if arr[i] != arr[n - i - 1]:
            count += 1

    # If the array is already palindromic, return 0
    if count == 0:
        return 0

    # Count the frequency of elements in the second half of the array
    second_half = n - first_half
    for i in range(first_half, first_half + second_half):
        if arr[i] != arr[n - i - 1]:
            count += 1

    # If the array is already palindromic, return 0
    if count == 0:
        return 0

    # Count the frequency of elements in the first half of the array
    for i in range(first_half):
        if arr[i] != arr[n - i - 1]:
            count += 1

    # If the array is already palindromic, return 0
    if count == 0:
        return 0

    # Count the frequency of elements in the second half of the array
    for i in range(first_half, first_half + second_half):
        if arr[i] != arr[n - i - 1]:
            count += 1

    return count