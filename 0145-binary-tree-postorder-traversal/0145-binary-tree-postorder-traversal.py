# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = root
        if r is None:
            return []
        a = [root.val]
        b = self.postorderTraversal(r.left)
        c = self.postorderTraversal(r.right)
        return b + c + a