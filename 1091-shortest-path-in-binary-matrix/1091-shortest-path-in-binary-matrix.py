class Solution(object):
    def shortestPathBinaryMatrix(self, grid):

        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        queue = [(0, 0, 1)]
        index = 0
        grid[0][0] = 1

        while index < len(queue):
            row, col, distance = queue[index]
            index += 1

            if row == n-1 and col == n-1:
                return distance
            for row_change in [-1, 0, 1]:
                for col_change in [-1, 0, 1]:

                    new_row = row + row_change
                    new_col = col + col_change

                    if 0 <= new_row < n and 0 <= new_col < n:
                        if grid[new_row][new_col] == 0:
                            grid[new_row][new_col] = 1
                            queue.append((new_row, new_col, distance + 1))

        return -1