def count_paths(m, n, blocks):
    ''' counting the number of paths from top left to bottom right.'''
    blocked = set(blocks)

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if (i, j) in blocked:
                dp[i][j] = 0
                continue

            if i == 0 and j == 0:
                continue

            ways = 0
            if i > 0:
                ways += dp[i - 1][j]
            if j > 0:
                ways += dp[i][j - 1]

            dp[i][j] = ways

    return dp[m - 1][n - 1]

if __name__ == "__main__":
    print(count_paths(3,4,[(0,3),(1,1)]))