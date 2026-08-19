# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        r = root
        if r is None:
            return []
        
        a= self.preorderTraversal(r.left)
        b = self.preorderTraversal(r.right)
        return [root.val] + a + b
        
