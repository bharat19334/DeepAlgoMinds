class Solution(object):
    def minimumChanges(self, s, k):
        
        n = len(s)
        cost = [[float('inf')] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                for d in range(1, length):
                    if length % d == 0:
                        changes = 0

                        for x in range(d):
                            left = i + x
                            right = i + x + ((length - 1 - x) // d) * d

                            while left < right:
                                if s[left] != s[right]:
                                    changes += 1

                                left += d
                                right -= d

                        cost[i][j] = min(cost[i][j], changes)

        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
