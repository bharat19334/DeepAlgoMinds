class Solution(object):
    def rob(self, nums):
        
    
        if len(nums) == 1:
            return nums[0]

        # 1st house include and last is not.
        dp1 = [0] *len(nums)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)- 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])

        ans1 = dp1[-2]

        # last in include but 1st is not.
        n = len(nums)
        dp2 = [0] * n
        dp2[1] = nums[1]
        if len(nums) > 2:
            dp2[2] = max(nums[1], nums[2])

        for i in range(3, len(nums)):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])

        ans2 = dp2[-1]
        return max(ans1,ans2)