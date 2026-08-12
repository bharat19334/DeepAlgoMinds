#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


class Solution:
    def isCircular(self, head):
        # code here
        
        if head is None:
            return True
        
        h1 = head
        temp = h1
        
        while h1 is not None:
            h1 = h1.next
            
            if temp == h1:
                return True
        return False