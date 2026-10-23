class Solution(object):
    def reverseBits(self, n):
        
        binary_str =""
        for i in range(32):
            binary_str += str(n%2)
            n = n//2
        
        ans = 0
        for n in range(32):
            ans = ans*2 + int(binary_str[n])

        return ans