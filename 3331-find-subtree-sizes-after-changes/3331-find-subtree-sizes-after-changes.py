class Solution(object):
    def findSubtreeSizes(self, parent, s):
        
        n = len(parent)
        adj = [[] for _ in range(n)]

        for i in range(1, n):
            adj[parent[i]].append(i)

        new = parent[:]
        last = {}
        def dfs(u):
            c = s[u]
            p = last.get(c, -1)

            if p != -1:
                new[u] = p
            last[c] = u

            for v in adj[u]:
                dfs(v)

            if p == -1:
                del last[c]
            else:
                last[c] = p

        dfs(0)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[new[i]].append(i)

        ans = [1] * n
        def calc(u):
            for v in adj[u]:
                calc(v)
                ans[u] += ans[v]
        calc(0)

        return ans