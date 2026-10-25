class Solution(object):
    def hasAlternatingBits(self, n):
        
        binary_num = ""
        while n>0:
            a = n%2
            binary_num += str(a)
            n = n//2
        
        binary_num = binary_num[::-1]
        for i in range(1, len(binary_num)):
            if binary_num[i] == binary_num[i - 1]:
                return False

        return True
        


