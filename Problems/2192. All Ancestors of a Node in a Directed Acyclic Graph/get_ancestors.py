from collections import defaultdict

class Solution:
    def getAncestors(self, n, edges):
        # create empty list for each node to add ancestors
        ancestors_list = [[] for _ in range(n)]

        # create a default dict to hold all connected ancestor edges
        g = defaultdict(list)

        # loop through edges and add ancestors to the node that they are connected too
        for start, end in edges:
            g[end].append(start)


        # depth first search
        def dfs(node, curr):
            # loop through the ancestors in the node
            for i in g[curr]:
                if i not in ancestors_list[node]:
                    dfs(node, i)
                    ancestors_list[node].append(i)


        for i in range(n):
            dfs(i, i)
        
        for k in ancestors_list:
            k.sort()

        return ancestors_list
