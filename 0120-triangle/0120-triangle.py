class Solution(object):
    def minimumTotal(self, triangle):
        
        # dp = [[0 for _ in range(len(triangle[i]))]for i in range(len(triangle))]
        # def solve(triangle,i, j): 
        #     if i==len(triangle)-1:
        #         return triangle[i][j]
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     left_path = solve(triangle,i+1,j)
        #     right_path = solve(triangle,i+1, j+1) 
        #     dp[i][j] = triangle[i][j]+ min(left_path, right_path)

        #     return dp[-1][-1]
        # return solve(triangle,0, 0)

        dp = triangle[-1][:]
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]