def move_one_ball(arr):
    if not arr:
        return True
    return arr == sorted(arr)