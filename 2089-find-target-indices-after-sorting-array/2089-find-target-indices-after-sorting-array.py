class Solution(object):
    def targetIndices(self, nums, target):
        
        arr = sorted(nums)
        ans = []
        for i in range(0,len(nums)):
            if arr[i] == target:
                ans.append(i)
        return ans
