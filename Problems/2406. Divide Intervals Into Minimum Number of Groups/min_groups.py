import heapq

class Solution:
    def minGroups(self, intervals):
        # initalize the heap
        pq = []

        # loop through the intervals
        for left, right in sorted(intervals):
            # if there are values and the heap and the first one is les than left
            if pq and pq[0] < left:
                # pop the value from the heap
                heapq.heappop(pq)
                # add to the heap
            heapq.heappush(pq, right)
        return len(pq)