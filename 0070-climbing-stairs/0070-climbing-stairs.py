class Solution:
    def climbStairs(self, n: int) -> int:
        # we will create a dp of n lenght
        dp = [0]*(n+1)
        dp[0]= 1
        dp[1] = 1

        # we will check from 2 because 0,1 step have only have single way
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]