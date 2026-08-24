# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # using queue
        que = []

        if root:
            que.append(root)
        while que:
            a = que.pop(0)
            a.left,a.right = a.right,a.left

            if a.left:
                que.append(a.left)
            if a.right:
                que.append(a.right)
        return root



            