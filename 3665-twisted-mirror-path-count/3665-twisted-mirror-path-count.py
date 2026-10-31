
class Solution(object):
    def uniquePaths(self, grid):

        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                # Right
                x = i
                y = j + 1
                down = True

                while x < m and y < n and grid[x][y] == 1:
                    if down:
                        x += 1
                    else:
                        y += 1
                    down = not down

                if x < m and y < n:
                    dp[x][y] = (dp[x][y] + dp[i][j]) % mod

                # Down
                x = i + 1
                y = j
                right = True

                while x < m and y < n and grid[x][y] == 1:
                    if right:
                        y += 1
                    else:
                        x += 1
                    right = not right

                if x < m and y < n:
                    dp[x][y] = (dp[x][y] + dp[i][j]) % mod

        return dp[-1][-1]