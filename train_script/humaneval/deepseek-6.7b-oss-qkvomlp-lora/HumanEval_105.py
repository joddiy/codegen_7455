def by_length(arr):
    # Filter the array to include only integers between 1 and 9 inclusive
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    
    # Sort the filtered array in ascending order
    sorted_arr = sorted(filtered_arr)
    
    # Reverse the sorted array
    reversed_arr = sorted_arr[::-1]
    
    # Map the integers to their corresponding names
    names = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    result = [names[num] for num in reversed_arr]
    
    return result