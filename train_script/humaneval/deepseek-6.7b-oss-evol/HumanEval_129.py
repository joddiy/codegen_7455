def minPath(grid, k):
    N = len(grid)
    path = [0] * k
    for i in range(k):
        path[i] = min((grid[i//N][i%N], i) for i in range(N*N))[1]
    return sorted([grid[i//N][i%N] for i in path])