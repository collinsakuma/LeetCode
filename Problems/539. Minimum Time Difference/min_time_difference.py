class Solution:
    def findMinDifference(self, timePoints):
        # convert times to minutes as an integer
        for index, time in enumerate(timePoints):
            timePoints[index] = int(time[:2]) * 60 + int(time[3:])

        timePoints.sort() # sort the times

        # because time is circular first and last time must be compared
        # compare the first and last time for a min time
        min_time = 1440 + timePoints[0] - timePoints[len(timePoints) - 1]

        # loop through range of time points
        for i in range(len(timePoints) - 1):
            # check time pairs for a lower minimum time
            min_time = min(min_time, abs(timePoints[i] - timePoints[i + 1]))

        return min_time