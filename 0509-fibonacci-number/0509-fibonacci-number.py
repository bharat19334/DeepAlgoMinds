class Solution(object):
    def fib(self, n):

        
        if n <= 1:
            return n
        # return self.fib(n-1) + self.fib(n-2)

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        i = 2

        while i <= n:
            dp[i] = dp[i - 1] + dp[i - 2]
            i += 1

        return dp[n]