class Solution(object):
    def countServers(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row = 0
                    col = 0
                    for k in range(n):
                        if grid[i][k] == 1:
                            row += 1
                    for k in range(m):
                        if grid[k][j] == 1:
                            col += 1
                    if row > 1 or col > 1:
                        count += 1

        return count