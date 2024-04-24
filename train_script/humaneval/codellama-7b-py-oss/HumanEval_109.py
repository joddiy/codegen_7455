def move_one_ball(arr):
    if not arr:
        return True
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))