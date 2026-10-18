class Solution(object):
    def numOfWays(self, nums):
        
        def N_o_w(arr):
            if len(arr) <= 2:
                return 1

            left = []
            right = []
            for i in range(1, len(arr)):
                if arr[i] < arr[0]:
                    left.append(arr[i])
                else:
                    right.append(arr[i])

            n = len(left) + len(right)
            r = len(left)
            ways = 1
            for i in range(r):
                ways = ways * (n - i) // (i + 1)

            return ways * N_o_w(left) * N_o_w(right) % (10**9 + 7)

        return (N_o_w(nums) - 1) % (10**9 + 7)