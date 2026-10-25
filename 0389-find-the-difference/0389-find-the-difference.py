class Solution(object):
    def findTheDifference(self, s, t):
        
        l1 = sorted(s)
        l2 = sorted(t)
        for i in range(0,len(s)):
            if l1[i] != l2[i]:
                return l2[i]

        return l2[-1]
        
        