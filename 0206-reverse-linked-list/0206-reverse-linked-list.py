# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 

        stack = []
        # it stores all node in tha stack
        while head:
            stack.append(head)
            head = head.next
        # for empty stack
        if not stack:
            return None

        # last node as a new head
        last_node = stack.pop()
        head = last_node

        # last node to head(None_
        while stack:
            head.next = stack.pop()
            head = head.next

        head.next = None

        return last_node