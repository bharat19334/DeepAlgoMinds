class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        matrix = obstacleGrid
        r = len(obstacleGrid)-1
        c = len(obstacleGrid[0])-1
        
        if matrix[0][0] == 1:
            return 0
            
        for i in range(0,r+1):
            for j in range(0,c+1):
                if i==0 and j == 0:
                    matrix[i][j] = 1
                elif matrix[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    if i>0 and j>0:
                        matrix[i][j] += matrix[i-1][j] + matrix[i][j-1]
                    elif i>0:
                        matrix[i][j] += matrix[i-1][j]
                    elif j>0:
                        matrix[i][j] += matrix[i][j-1]

        return matrix[r][c]