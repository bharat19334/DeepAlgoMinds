# 75 DAYS GFG POTD ARTICLE CHALLENGE CHALLENGE(DAY 44/75)

## Problem

This problem is from GeeksforGeeks.

## Difficulty

**Not specified**

## Source

[GeeksforGeeks](https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1)

## Solution

```python
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
```

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Language

Python 3
