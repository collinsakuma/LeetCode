from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges):
        g = defaultdict(list)
        
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = 0
        subtree = {}

        def dfs(node, prev, depth):
            total = 1
            # use nonlocal to get access to ans variable in the nested dfs function
            nonlocal ans
            ans += depth

            for child in g[node]:
                if child == prev:
                    continue
                total += dfs(child, node, depth + 1)

            subtree[node] = total

            return total