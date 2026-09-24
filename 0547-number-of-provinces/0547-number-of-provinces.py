class Solution(object):
    def findCircleNum(self, isConnected):
        
        n = len(isConnected)
        seen = [False] * n
        ans = 0

        for i in range(n):
            if seen[i] == False:
                ans += 1
                stack = [i]
                seen[i] = True

                while stack:
                    city = stack.pop()

                    for j in range(n):
                        if isConnected[city][j] == 1 and seen[j] == False:
                            seen[j] = True
                            stack.append(j)
        return ans




