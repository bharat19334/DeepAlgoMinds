class Solution(object):
    def targetIndices(self, nums, target):
        
        for i in range(len(nums)):
            min_idx = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j

            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        # arr = sorted(nums)
        arr = nums
        ans = []
        for i in range(0,len(nums)):
            if arr[i] == target:
                ans.append(i)
        return ans

