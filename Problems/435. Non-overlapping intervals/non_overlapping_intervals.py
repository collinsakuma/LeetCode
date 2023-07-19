class Solution:
    def eraseOverlapIntervals(self, intervals):
        
        def get_second(interval): # helper function for the sort() to return the end time of each interval 
            return interval[1]
        
        intervals.sort(key = get_second) # sort the interval using the endtime of each interval as the key
        n = len(intervals)

        prev = 0
        count = 1

        for i in range(1, n):
            if intervals[i][0] >= intervals[prev][1]: # compare the next interval with the previous one checking if the begining time of the next is at the same time or after the ending time of the previous. 
                prev = i # update previous if times are not overlapping
                count += 1 # increment count to show that one interval is okay

        return n - count # return number of intervals that cannot be attention by minusing total intervals by the count of intervals with non overlapping times