import heapq

def minPath(grid, k):
    n = len(grid)
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    heap = [(grid[0][0], 0, 0)]
    visited = set((0,0))
    while heap:
        val, x, y = heapq.heappop(heap)
        if (x, y) == (n-1, n-1) and k == 0:
            return [val]
        if k > 0:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(heap, (grid[nx][ny], nx, ny))
            k -= 1
    return []