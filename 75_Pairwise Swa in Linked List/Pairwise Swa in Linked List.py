''' Structure of linked list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def pairwiseSwap(self, head):
        
        temp = Node(0)
        temp.next = head
        h = temp

        while h.next and h.next.next:

            a = h.next
            b = a.next

            a.next = b.next
            b.next = a
            h.next = b

            h = a
        return temp.next
