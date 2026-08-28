# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        
        if not root:
            return None

        t = root
        if t.val == key:
            if t.left == None:
                return t.right
            if t.right == None:
                return t.left

            maxNode = t.left

            while maxNode.right:
                maxNode = maxNode.right

            t.val = maxNode.val
            t.left = self.deleteNode(t.left, maxNode.val)

        elif key < t.val:
            t.left = self.deleteNode(t.left, key)
        else:
            t.right = self.deleteNode(t.right, key)

        return t