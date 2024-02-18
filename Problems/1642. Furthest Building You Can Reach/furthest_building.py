import heapq

class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        n = len(heights)
        heap = []

        for i in range(1, n):
            distance = heights[i] - heights[i - 1]

            if distance > 0:
                heapq.heappush(heap, distance)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
                if bricks < 0:
                    return i - 1
                
        return n - 1 