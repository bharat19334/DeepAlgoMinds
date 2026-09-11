class Solution:
    def wallsAndGates(self, rooms):

        r_len = len(rooms)
        c_len = len(rooms[0])
        INF = 2**31 - 1
        que = []
        for row in range(r_len):
            for col in range(c_len):
                if rooms[row][col] == 0:
                    que.append((row, col))

        while que:
            row, col = que.pop(0)

            # We check the top side
            if row - 1 >= 0 and rooms[row - 1][col] == INF:
                rooms[row - 1][col] = rooms[row][col] + 1
                que.append((row - 1, col))

            # We check the bottom side
            if row + 1 < r_len and rooms[row + 1][col] == INF:
                rooms[row + 1][col] = rooms[row][col] + 1
                que.append((row + 1, col))

            # We check the left side
            if col - 1 >= 0 and rooms[row][col - 1] == INF:
                rooms[row][col - 1] = rooms[row][col] + 1
                que.append((row, col - 1))

            # We check the right side
            if col + 1 < c_len and rooms[row][col + 1] == INF:
                rooms[row][col + 1] = rooms[row][col] + 1
                que.append((row, col + 1))
