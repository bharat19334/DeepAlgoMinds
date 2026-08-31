# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        
        if root == None:
            return 0

        q = [(root, 0)]
        ans = 0

        while q:
            width = q[-1][1] - q[0][1] + 1

            if width > ans:
                ans = width
                
            for _ in range(len(q)):
                node, i = q.pop(0)
                if node.left:
                    q.append((node.left, i * 2))
                if node.right:
                    q.append((node.right, i * 2 + 1))

        return ans