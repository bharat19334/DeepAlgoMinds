class Solution:
    def floorSqrt(self, n): 
        # code here
        left =0
        right = n
        ans = 0
        while left <= right:
            
            mid = left + (right-left)//2
            if mid*mid == n:
                return mid
            if mid*mid < n:
                ans = mid
                left = mid +1
            else:
                right = mid -1
            
        return ans