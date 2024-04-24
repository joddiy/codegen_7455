import math

def max_fill(grid, capacity):
    rows, cols = len(grid), len(grid[0])
    total_water = sum(sum(row) for row in grid)
    bucket_count = math.ceil(total_water / capacity)
    return bucket_count