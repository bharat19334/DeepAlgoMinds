class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Create a dp array of length n initialized with 0
        dp = [0]*len(cost)
        # we have minimum cost to reach the first two stairs
        dp[0] = cost[0]
        dp[1] = cost[1]
        n = len(cost)

        for i in range(2,n):
            # current cost + from previous two stairs minimum cost
            dp[i] = cost[i] + min(dp[i-2],dp[i-1])

        return min(dp[n-1],dp[n-2])

