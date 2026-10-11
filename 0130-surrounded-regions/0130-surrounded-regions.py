class Solution(object):
    def solve(self, board):
        
        r = len(board)
        c = len(board[0])
        que = []

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == r-1 or j == c-1):
                    que.append((i, j))
                    board[i][j] = '#'

        while que:

            i, j = que.pop()
            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < r and 0 <= y < c and board[x][y] == 'O':
                    board[x][y] = '#'
                    que.append((x, y))

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'