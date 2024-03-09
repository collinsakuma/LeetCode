from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums):
        # initialize max frequency counter 
        max_frequency = 0
        count = Counter(nums) # create dict of nums with count of each number as value 

        # sort the count by the value
        count = sorted(count.items(), key=lambda item: item[1])
        # set frequency to the highest frequency in nums
        frequency = count[-1][-1]

        # loop though range of count
        for i in range(len(count)):
            # if the number has the max frequency in nums 
            if count[i][1] == frequency:
                # increase max_frequency by frequency
                max_frequency += frequency

        return max_frequency