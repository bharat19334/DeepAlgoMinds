class Solution(object):
    def longestPalindromeSubseq(self, s):
        
        # def LPS(s,start,end):
        #     if start > end:
        #         return 0   
        #     if start == end:
        #         return 1
        #     elif s[start] == s[end]:
        #         return 2+ LPS(s,start+1,end-1)
        #     else:
        #         return max(LPS(s,start+1,end),LPS(s,start,end-1))
        # return LPS(s,0,len(s)-1)

        dp= [[-1 for i in range(len(s))] for i in range(len(s))]

        def LPS(s,start,end):
            if start > end:
                return 0  
            if start == end:
                return 1

            if dp[start][end]!= -1:
                return dp[start][end]
            elif s[start] == s[end]:
                dp[start][end] =2+ LPS(s,start+1,end-1)
            else:
                dp[start][end] = max(LPS(s,start+1,end),LPS(s,start,end-1))
            
            return dp[start][end]

        return LPS(s,0,len(s)-1)





        
            