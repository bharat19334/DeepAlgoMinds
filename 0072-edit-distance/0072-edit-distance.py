
class Solution(object):
    def minDistance(self, word1, word2):

        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

        for i in range(l2 + 1):
            dp[0][i] = i
        for i in range(l1 + 1):
            dp[i][0] = i

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert = dp[i][j - 1]
                    delete = dp[i - 1][j]
                    replace = dp[i - 1][j - 1]
                    
                    dp[i][j] = 1 + min(insert, delete, replace)

        return dp[-1][-1]
