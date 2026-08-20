# Triplets with Sum in Range

Given an array **arr[]** and a range from **l** to **r**, the task is to count the number of triplets having a sum in the range `[l, r]`.

## Examples

### Example 1

text
Input: arr = [8, 3, 5, 2], l = 7, r = 11
Output: 1

Explanation:
There is only one triplet [2, 3, 5] having sum 10 in range [7, 11].

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
