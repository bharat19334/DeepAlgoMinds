class Solution(object):
    def minSwaps(self, nums):
        
        arr = []
        for i in range(len(nums)):
            total = 0
            a = str(nums[i])
            for j in range(len(a)):
                total += int(a[j])

            arr.append((total, nums[i]))

        arr.sort()

        target = []
        for i in range(len(arr)):
            target.append(arr[i][1])

        n = len(nums)
        pos = {}

        for i in range(n):
            pos[nums[i]] = i

        count = 0
        for i in range(n):
            if nums[i] != target[i]:

                j = pos[target[i]]

                pos[nums[i]] = j
                pos[nums[j]] = i
                nums[i], nums[j] = nums[j], nums[i]
                count += 1

        return count