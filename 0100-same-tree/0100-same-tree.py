# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        t1 = p
        t2 = q

        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False

        if t1.val != t2.val:
            return False
        a = self.isSameTree(t1.left,t2.left)
        b = self.isSameTree(t1.right,t2.right)
        return a and b