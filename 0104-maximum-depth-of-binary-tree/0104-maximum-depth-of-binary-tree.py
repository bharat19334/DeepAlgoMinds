# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        t = root
        if t == None:
            return 0
        
        l = self.maxDepth(t.left)
        r= self.maxDepth(t.right)
        
        if l > r:
            return l + 1
        else:
            return r + 1
        