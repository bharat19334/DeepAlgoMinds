# Sorted and Rotated Minimum

## Problem

This problem is from GeeksforGeeks.

## Difficulty

**Not specified**

## Source

[GeeksforGeeks](https://www.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/1)

## Solution

```python
class Solution:
    def findMin(self, arr):
        # code here
        
        min_val = arr[0]
        for i in range(0,len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]
        return min_val
                
```

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Language

Python 3
