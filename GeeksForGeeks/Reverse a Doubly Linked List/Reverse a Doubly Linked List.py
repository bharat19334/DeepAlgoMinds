""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        
        h = head
        while h:
            # it will swap the next and previous nodes 
            h.prev,h.next = h.next,h.prev
            # it will make current node as a new node
            head = h
            h = h.prev
            
        # it will return the new Node
        return head
            
