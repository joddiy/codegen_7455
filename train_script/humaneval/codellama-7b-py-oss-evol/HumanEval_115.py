def max_fill(grid, capacity):
    # Calculate the total number of wells
    total_wells = sum(row.count(1) for row in grid)

    # Calculate the number of times we need to lower the buckets
    return total_wells // capacity