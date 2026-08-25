# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        t = root

        while t:
            if t.val == val:
                return t
            if val > t.val:
                t = t.right
            else:
                t = t.left

        return None
