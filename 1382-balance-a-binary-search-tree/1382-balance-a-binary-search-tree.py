# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        
        ans = []
        
        def inorder(root):
            if root != None:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)
        
        inorder(root)
        
        def bin_search(start, end):
            if start > end:
                return None
            
            mid = (start + end) // 2
            node = TreeNode(ans[mid])  
            node.left = bin_search(start, mid - 1)
            node.right = bin_search(mid + 1, end)
            
            return node
      
        return bin_search(0, len(ans) - 1)
        