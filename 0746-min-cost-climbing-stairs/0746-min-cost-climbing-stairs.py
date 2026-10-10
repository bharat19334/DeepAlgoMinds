class Solution(object):
    def minCostClimbingStairs(self, cost):
        
        n = len(cost)
        dp = [0]*(n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)+1):
            if i== n:
                dp[i] = min(dp[i-2],dp[i-1])
            else:
                dp[i] = min(dp[i-1],dp[i-2]) + cost[i]

        return dp[n]