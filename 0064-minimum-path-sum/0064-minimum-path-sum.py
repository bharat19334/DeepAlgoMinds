class Solution(object):
    def minPathSum(self, grid):
        
        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if r == 0 and c == 0:
                    grid[r][c] = grid[r][c]
                elif r == 0:
                    grid[r][c] += grid[r][c-1]
                elif c == 0:
                    grid[r][c] += grid[r-1][c]
                else:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])

        return grid[row-1][col-1]
