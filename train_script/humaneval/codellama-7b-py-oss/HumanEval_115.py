def max_fill(grid, capacity):
    def get_water(row, col, capacity):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        if grid[row][col] == 1:
            return 0
        grid[row][col] = 1
        return 1 + get_water(row + 1, col, min(capacity, grid[row][col])) + \
               get_water(row - 1, col, min(capacity, grid[row][col])) + \
               get_water(row, col + 1, min(capacity, grid[row][col])) + \
               get_water(row, col - 1, min(capacity, grid[row][col]))

    total_water = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                total_water += get_water(i, j, capacity)
    return total_water