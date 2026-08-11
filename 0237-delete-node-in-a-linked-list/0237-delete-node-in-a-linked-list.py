# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        temp_node = node.next
        # this is Copying the next node value into the current node
        node.val = temp_node.val
        # This is skipping the next node
        node.next = temp_node.next
        