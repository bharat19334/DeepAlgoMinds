# Triplets with Sum in Range

## Problem

This problem is from GeeksforGeeks.

## Difficulty

**Not specified**

## Source

[GeeksforGeeks](https://www.geeksforgeeks.org/problems/triplets-with-sum-with-given-range/1)

## Solution

```python
class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        
        # Brute force
        
        count = 0
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if l <= arr[i]+arr[j]+arr[k] <= r:
                        count +=1
        return count
        
        
```

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Language

Python 3
