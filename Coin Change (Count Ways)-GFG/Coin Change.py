class Solution:
    def count(self, coins: list[int], sum: int) -> int:
        # code here
        
        dp = [0] * (sum + 1)
        dp[0] = 1

        for c in coins:
            for i in range(c, sum + 1):
                dp[i] += dp[i - c]

        return dp[-1]
                
