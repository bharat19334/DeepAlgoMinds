# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        q = [root]
        ans = []
        i = 0
        while q:
            a = []
            for j in range(len(q)):
                r = q.pop(0)
                a.append(r.val)

                if r.left:
                    q.append(r.left)

                if r.right:
                    q.append(r.right)
            if i:
                a.reverse()

            ans.append(a)
            # it will Change our i to 0 or 1 for every level
            i = 1 - i
        return ans