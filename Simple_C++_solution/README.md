# Simple C++ solution:

## Problem

This problem is from GeeksforGeeks.

## Difficulty

**Not specified**

## Source

[GeeksforGeeks](https://www.geeksforgeeks.org/problems/count-1s-in-binary-array-1587115620/1)

## Solution

```python
class Solution:
    def countOnes(self, arr):
        
        count = 0
        i=0
        while i<len(arr):
            if arr[i]==1:
                count +=1
            i+=1
        return count
```

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Language

Python 3
