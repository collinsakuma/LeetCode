class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        output = 0 # set variable to keep track of how long ashe is poisoned
        for i in range(len(timeSeries) - 1): # loop through range of the timeSeries( attacks )
            # for the attack at i check if the duration that ashe will be poionsed for overlaps with the next attack
            if timeSeries[i] + (duration - 1) < timeSeries[i + 1]: 
                # if there is no overlap then ashe will be poisoned for the entire duration 
                output += duration
            # check if the attack overlaps with the next attack
            elif timeSeries[i] + (duration - 1) >= timeSeries[i + 1]:
                # if there is an overlap then only add the difference between the two attacks
                output += timeSeries[i + 1] - timeSeries[i]
        # for the last attack performed ashe will be poisoned for the whole duration, add entire duration to output
        output += duration 
        
        return output # return duration of seconds that ashe is poisoned for