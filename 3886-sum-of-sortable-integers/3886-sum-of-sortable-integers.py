class Solution(object):
    def sortableIntegers(self, nums):

        n = len(nums)
        total = 0
        for k in range(1, n + 1):
            if n % k != 0:
                continue

            is_valid = True
            previous = None
            for i in range(0, n, k):
                arr = nums[i:i + k]
                count = 0
                start = 0
                for j in range(k):
                    next_index = (j + 1) % k
                    if arr[j] > arr[next_index]:
                        count += 1
                        start = next_index

                if count > 1:
                    is_valid = False
                    break
                first = arr[start]
                last = arr[(start - 1) % k]

                if previous is not None and previous > first:
                    is_valid = False
                    break

                previous = last

            if is_valid:
                total += k

        return total