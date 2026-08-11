# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        L1 = list1
        L2 = list2
        new_node = ListNode(0)
        current_node = new_node

        while L1 and L2:
            # it will check our value of L1 node 1 is less from L2 node 1.
            if L1.val <= L2.val:
                current_node.next = L1
                L1 = L1.next

            elif L1.val > L2.val:
                current_node.next = L2
                L2 = L2.next
            
            current_node = current_node.next
        
        if L1:
            current_node.next = L1
        else:
            current_node.next = L2
        return new_node.next
