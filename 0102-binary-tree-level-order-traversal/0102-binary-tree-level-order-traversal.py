# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):

        if not root:
            return []

        ans = [] 
        q = [root]

        while q:
            temp = []

            for _ in range(len(q)):
                x = q.pop(0)
                temp.append(x.val)

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

            ans.append(temp)

        return ans
        