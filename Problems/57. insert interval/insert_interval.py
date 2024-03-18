class Solution:
    def insert(self, intervals, newInterval):
        result = []

        for interval in intervals:
            # if the interval does not overlap with the newInterval add it to the interval list
            if interval[1] < newInterval[0]:
                result.append(interval)
            # if the newInterval is before interval add the newInterval to the list
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval # set a new newInterval
            # if the two interval overlaps with eachother
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                # create a new interval with the min and max of both intervals
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        result.append(newInterval)
        return result