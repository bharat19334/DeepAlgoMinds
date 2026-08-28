# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        
        if root is None:
            return 0

        t = root
        ans = 0
        if low <= t.val <= high:
            ans += t.val

        ans += self.rangeSumBST(root.left, low, high)
        ans += self.rangeSumBST(root.right, low, high)

        return ans
        