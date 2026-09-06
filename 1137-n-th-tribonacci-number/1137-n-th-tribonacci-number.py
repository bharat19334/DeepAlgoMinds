class Solution(object):
    def tribonacci(self, n):
        
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        t0 = 0
        t1 = 1
        t2 = 1
        i=3
        while i <= n:
            t3 = t0+t1+t2
            t0,t1,t2 = t1,t2,t3
            i+=1
        return t3