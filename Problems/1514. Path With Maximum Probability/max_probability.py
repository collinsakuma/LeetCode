from collections import defaultdict, deque

class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        # map out the
        graph, dq = defaultdict(list), deque([start_node])

        for i, (a, b) in enumerate(edges):
            graph[a].append([b, i])
            graph[b].append([a, i])

        p = [0.0] * n
        p[start_node] = 1.0

        while dq:
            curr = dq.popleft()
            for neighbor, i in graph[curr]:
                if p[curr] * succProb[i] > p[neighbor]:
                    p[neighbor] = p[curr] * succProb[i]
                    dq.append(neighbor)

        return p[end_node]