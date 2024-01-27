import heapq

class Solution:
    def minStoneSum(self, piles, k):
        pq = [-x for x in piles]
        heapq.heapify(pq)
        for i in range(k):
            heapq.heapreplace(pq, pq[0] // 2)

        return -sum(pq)