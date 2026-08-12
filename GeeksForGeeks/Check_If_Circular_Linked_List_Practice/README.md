# Check If Circular Linked List | Practice

## Problem

This problem is taken from GeeksforGeeks.

## Difficulty

**Not specified**

## Source

[GeeksforGeeks](https://www.geeksforgeeks.org/problems/circular-linked-list/1)

## Solution

```python
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
```

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Language

Python 3
