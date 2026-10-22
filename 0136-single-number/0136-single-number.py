class Solution(object):
    def singleNumber(self, nums):
        
        # hash_dict = {}
        # for i in range(0,len(nums)):
        #     hash_dict[nums[i]] = hash_dict.get(nums[i],0)+1

        # for k,v in hash_dict.items():
        #     if v == 1:
        #         return k

        ans = 0

        for num in nums:
            ans = ans ^ num

        return ans

        
