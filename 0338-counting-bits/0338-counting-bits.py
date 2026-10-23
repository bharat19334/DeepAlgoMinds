class Solution(object):
    def countBits(self, n):
        
        ans = []
        i = 0
        while i<=n:
            num =i
            count = 0
            
            while num>0:
                a = num%2
                if a == 1:
                    count += 1
                num = num//2

            ans.append(count)
            i += 1

        return ans
