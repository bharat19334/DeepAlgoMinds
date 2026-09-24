class Solution(object):
    def floodFill(self, image, sr, sc, color):
      
        pix_matrix = image
        curr_color = pix_matrix[sr][sc]

        if curr_color == color:
            return pix_matrix

        stack = [(sr, sc)]

        while stack:
            r, c = stack.pop()

            if r < 0:
                continue
            if r >= len(pix_matrix):
                continue
            if c < 0:
                continue
            if c >= len(pix_matrix[0]):
                continue
            if pix_matrix[r][c] != curr_color:
                continue

            pix_matrix[r][c] = color

            stack.append((r + 1, c))
            stack.append((r - 1, c))
            stack.append((r, c + 1))
            stack.append((r, c - 1))  

        return pix_matrix