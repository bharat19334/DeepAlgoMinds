# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        if root == None:
            return []

        ans = []
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(0,n):
                p = queue.pop(0)
                
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
                if i == (n-1):
                    ans.append(p.val)

        return ans
        

