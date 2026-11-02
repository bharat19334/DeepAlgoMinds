class Solution(object):
    def minMoves2(self, nums):
        
        nums.sort()
        mid = len(nums) // 2
        target = nums[mid]
        moves = 0

        for num in nums:
            moves += abs(num - target)

        return moves