class Solution(object):
    def reverseBits(self, n):
        
        binary_num = ""
        for i in range(32):
            binary_num = str(n%2)+binary_num
            n = n//2

        ans = 0
        for i in range(31,-1,-1):
            ans = ans*2 +int(binary_num[i])

        return ans