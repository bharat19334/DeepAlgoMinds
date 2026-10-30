class Solution(object):
    def getSum(self, a, b):
        
        mask = 0xFFFFFFFF
        while b:
            carry = (a&b)<<1
            a = (a^b) & mask
            b = carry & mask

        if a>0x7FFFFFFF:
            return ~(a ^ mask)

        return a