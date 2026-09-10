class Solution(object):
    def numIslands(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == "1":
                    count += 1

                    stack = [(i, j)]
                    grid[i][j] = "0"

                    while stack:
                        row, col = stack.pop()

                        if row > 0 and grid[row-1][col] == "1":
                            grid[row-1][col] = "0"
                            stack.append((row-1, col))

                        if row < m-1 and grid[row+1][col] == "1":
                            grid[row+1][col] = "0"
                            stack.append((row+1, col))

                        if col > 0 and grid[row][col-1] == "1":
                            grid[row][col-1] = "0"
                            stack.append((row, col-1))

                        if col < n-1 and grid[row][col+1] == "1":
                            grid[row][col+1] = "0"
                            stack.append((row, col+1))

        return count