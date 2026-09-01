# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        node = root
        ans = []
        def inorder_trav(node):
            if node == None:
                return 
            inorder_trav(node.left)
            ans.append(node.val)
            inorder_trav(node.right)

        inorder_trav(root)
        return ans