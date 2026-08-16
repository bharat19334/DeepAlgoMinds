class Solution:
    def findMin(self, arr):
        # code here
        
        min_val = arr[0]
        for i in range(0,len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]
        return min_val
                