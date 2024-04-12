import heapq

class Solution:
    # iniitlaize SeatManger class with a counter variable ( next ) that represents the next available seat
    # initalize an empty list that will be used as the heap
    def __init__(self, n):
        self.next = 1
        self.heap = []

    def reserve(self):
        # check if there are unreseared seats in the heap
        # and if the first unresearved seat in the heap is a lower number seat than the next available
        if self.heap and self.heap[0] < self.next:
            return heapq.heappop(self.heap)
        # if heap has no available seats or the first avaialbe in the heap isnt a lower numbered seat assign the next seat
        self.next += 1
        return self.next - 1
    
    def unreserved(self, seatNumber):
        # seat number is added to the back of the heap ensuring seats will be allocated in assecnding order
        heapq.heappush(self.heap, seatNumber)