# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        
        stack = []
        total = 0
        t = root

        while t or stack:
        
            while t:
                stack.append(t)
                t = t.right

            t = stack.pop()
            total = total + t.val
            t.val = total
            t = t.left

        return root
        