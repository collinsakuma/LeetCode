class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()

        i = 0
        maximize_capital = []

        while k > 0:
            while i < n and projects[i][0] <= w:
                heapq.heappush(maximize_capital, -projects[i][1])
                i += 1
            if not maximize_capital:
                break
            w-= heapq.heappop(maximize_capital)
            k -= 1
        return w