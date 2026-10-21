class Solution(object):
    def minOperations(self, s):
        
        n = len(s)

        if s == ''.join(sorted(s)):
            return 0

        if n == 2:
            return -1

        minn = min(s)
        maxx = max(s)

        if s[0] == minn or s[-1] == maxx:
            return 1

        for i in range(1, n - 1):
            if s[i] == minn or s[i] == maxx:
                return 2

        return 3

        