# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        queue = [(root, 0)]
        max_width = 0

        while queue:
            size = len(queue)
            first = queue[0][1]
            last = queue[-1][1]

            max_width = max(max_width, last - first + 1)

            for i in range(size):
                node, index = queue.pop(0)

                if node.left:
                    queue.append((node.left, index * 2))

                if node.right:
                    queue.append((node.right, index * 2 + 1))

        return max_width
        