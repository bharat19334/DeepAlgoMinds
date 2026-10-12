class Solution(object):
    def numDecodings(self, s):
        
        a = [0] * (len(s) + 1)
        a[0] = 1

        for i in range(1, len(s) + 1):
            if s[i-1] != '0':
                a[i] = a[i-1]

            if i > 1 and s[i-2] == '1' or i > 1 and s[i-2] == '2' and s[i-1] <= '6':
                a[i] += a[i-2]

        return a[-1]