class Solution(object):
    def hammingWeight(self, n):
        
        count = 0
        while n > 0:
            
            reminder = n % 2
            if reminder == 1:
                count += 1

            n = n // 2
        return count