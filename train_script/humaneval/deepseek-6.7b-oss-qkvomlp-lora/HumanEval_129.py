def minPath(grid, k):
    def dfs(i, j, path, visited):
        if len(path) == k:
            return path
        if (i, j) in visited:
            return None
        visited.add((i, j))
        min_path = None
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                new_path = dfs(ni, nj, path + [grid[ni][nj]], visited)
                if new_path is not None and (min_path is None or new_path < min_path):
                    min_path = new_path
        visited.remove((i, j))
        return min_path

    n = len(grid)
    min_path = None
    for i in range(n):
        for j in range(n):
            path = dfs(i, j, [grid[i][j]], set())
            if path is not None and (min_path is None or path < min_path):
                min_path = path
    return min_path