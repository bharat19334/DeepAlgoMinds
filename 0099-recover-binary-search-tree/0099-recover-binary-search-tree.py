# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        
        nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        inorder(root)

        first = None
        sec = None
        prev = None
        for i in range(len(nodes)-1):
            if nodes[i].val > nodes[i+1].val:
                if first is None:
                    first = nodes[i]
                sec = nodes[i+1]
        first.val, sec.val = sec.val, first.val