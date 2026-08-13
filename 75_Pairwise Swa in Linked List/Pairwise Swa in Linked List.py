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
        h1 = temp

        while h1.next and h1.next.next:

            a = h1.next
            b = a.next

            a.next = b.next
            b.next = a
            h1.next = b
            h1 = a
        return temp.next
