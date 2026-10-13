class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        dp = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]

        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1

        # it will fill the first column = 1
        for i in range(1,len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = 0
        # it wil fill the first row = 1
        for i in range(1,len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0 
        
        for r in range(1,len(obstacleGrid)):
            for c in range(1,len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[-1][-1]

                


        
        