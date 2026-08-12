# Reverse a Doubly Linked List

## Problem

This problem is taken from GeeksforGeeks.

## Difficulty

**Not specified**

## Source

[GeeksforGeeks](https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1)

## Solution

```python
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
            
```

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Language

Python 3
