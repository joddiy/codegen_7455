def sort_array(array):
    if not array:
        return array
    else:
        sum_value = array[0] + array[-1]
        if sum_value % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)