# Doubly Linked List Traversal | Practice

## Problem

This problem is taken from GeeksforGeeks.

## Difficulty

**Not specified**

## Source

[GeeksforGeeks](https://www.geeksforgeeks.org/problems/display-doubly-linked-list--154650/1)

## Solution

```python
''' Structure of doubly linked list Node
  class Node:
      def __init__(self, x):
          self.data = x
          self.next = None
          self.prev = None
'''
class Solution:
    def displayList(self, head):
        # code here
        
       
        forword = []
        backword = []
        h1 = head
        temp = None
        
        while h1:
            forword.append(h1.data)
            temp = h1
            h1 = h1.next
            
        while temp:
            backword.append(temp.data)
            temp = temp.prev
        
            
        return [forword,backword]
            
            
```

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Language

Python 3
