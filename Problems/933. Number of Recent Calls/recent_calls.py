from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque() # set up a deque list to use for finding the amount of pings in the 3000 ms interval

    def ping(self, t):
        queue = self.queue # set the que
        start = t - 3000 # the start time for the past 3000 ms before t
        queue.append(t) # append t to the queue as it is the last call made 

        while(queue and queue[0] < start):
            # loop though the queue and remove time interval from the left side of the list untill either queue has no more numbers in the list or the left most element is greater than the start time (element is within the last 3000 ms)
            queue.popleft()
        return len(queue)