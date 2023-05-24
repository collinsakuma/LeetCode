import heapq  # heapq is a library for heap priority que data structure.  

class KthLargest:

    def __init__(self, k, nums):
        self.heap = nums  # sets a heap variable to the list of numbers.  
        self.k = k
        heapq.heapify(self.heap)  # heapify arranges the list into a heap priority que. 
        while len(self.heap) > k:
            heapq.heappop(self.heap)  # pops and returns the smallest item from the heap. 

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)  
            # adding the value from nums into the heap. heappush will add val to the heap and
            # simultaneously rearrange organize the heap into a new prioroty que. 
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]