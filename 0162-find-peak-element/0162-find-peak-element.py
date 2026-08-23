class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        
        n = len(nums)
        # for i in range(0,n-1):
        #     if nums[i] > nums[i+1]:
        #         return i
        # return n-1

        left = 0
        right = n-1

        while left<right:
            mid = left + (right-left)//2
            
            if nums[mid] < nums[mid+1]:
                left = mid +1
            else:
                right = mid
        return left


