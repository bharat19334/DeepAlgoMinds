class Solution(object):
    def maxSubArray(self, nums):
        
        total = 0
        max_sub = float("-inf")
        
        for i in range(0,len(nums)):
            total += nums[i]
            
            if total > max_sub:
                max_sub = total

            if total < 0:
                total = 0
        return max_sub