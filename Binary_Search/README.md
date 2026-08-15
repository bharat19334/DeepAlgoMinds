# Binary Search

## Problem

This problem is from GeeksforGeeks.

## Difficulty

**Not specified**

## Source

[GeeksforGeeks](https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1)

## Solution

```python
class Solution:
    def binarySearch(self, arr, k):
        # code here
        
        left = 0
        right = len(arr)-1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if arr[mid] == k:
                return True
            if arr[mid] < k:
                left = mid + 1
            else:
                right = mid -1
        return False
                
                
```

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Language

Python 3
