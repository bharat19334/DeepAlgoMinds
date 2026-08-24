# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def func(node):
            if node == None:
                return 0

            left = func(node.left)
            right = func(node.right)

            if left < 0 or right < 0:
                return -1
            if abs(left - right) <= 1:
                return max(left, right) + 1

            return -1
        return func(root) != -1