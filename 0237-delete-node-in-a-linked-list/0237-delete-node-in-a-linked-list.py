# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # this is Copying the next node's value into the current node
        node.val = node.next.val
        # This is skipping the next node
        node.next = node.next.next
        