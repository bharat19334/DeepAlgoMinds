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
                        x, y = stack.pop()

                        if x > 0 and grid[x-1][y] == "1":
                            grid[x-1][y] = "0"
                            stack.append((x-1, y))

                        if x < m-1 and grid[x+1][y] == "1":
                            grid[x+1][y] = "0"
                            stack.append((x+1, y))

                        if y > 0 and grid[x][y-1] == "1":
                            grid[x][y-1] = "0"
                            stack.append((x, y-1))

                        if y < n-1 and grid[x][y+1] == "1":
                            grid[x][y+1] = "0"
                            stack.append((x, y+1))

        return count