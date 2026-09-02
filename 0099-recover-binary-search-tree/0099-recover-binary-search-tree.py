# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        
        nodes = []

        def inorder(curr_node):
            if not curr_node:
                return
            inorder(curr_node.left)
            nodes.append(curr_node)
            inorder(curr_node.right)
            
        inorder(root)

        first = None
        second = None
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                if first == None:
                    first = nodes[i]
                second = nodes[i + 1]

        first.val, second.val = second.val, first.val