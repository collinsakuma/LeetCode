from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        def find(graph, x, y, d):
            if (x, y) in d:
                return d[(x, y)]
            
            pq, visit = [], set()
            heapq.heappush(pq, (0, x))

            while pq:
                cost, node = heapq.heappop(pq)
                if node == y:
                    return cost
                if node in visit:
                    continue
                visit.add(node)
                for ne, new_cost in graph[node]:
                    heapq.heappush(pq, (cost + new_cost, ne))
            return -1

        n = len(source)

        graph = defaultdict(list)
        for x, y, z in zip(original, changed, cost):
            graph[x].append([y, z])

        res, d = 0, {}

        for i in range(n):
            val = find(graph, source[i], target[i], d)
            if val == -1:
                return -1
            else:
                res += val
            d[(source[i], target[i])] = val

        return res