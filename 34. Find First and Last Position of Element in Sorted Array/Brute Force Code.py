# Brute Force
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first = -1
        last = -1
        i = 0
        j = len(nums) - 1

        while i <= j:

            if nums[i] == target and first == -1:
                first = i
            else:
                i += 1

            if nums[j] == target and last == -1:
                last = j
            else:
                j -= 1

        return [first, last]
