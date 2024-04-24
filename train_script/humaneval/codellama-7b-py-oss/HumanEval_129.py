def minPath(grid, k):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = grid[i][j]

    for _ in range(k - 1):
        new_dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_dp[i][j] = dp[i][j]
                if i > 0:
                    new_dp[i][j] += dp[i - 1][j]
                if j > 0:
                    new_dp[i][j] += dp[i][j - 1]
        dp = new_dp

    ans = []
    for i in range(n):
        for j in range(n):
            ans.append(dp[i][j])
    return sorted(ans)