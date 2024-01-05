from collections import Counter

class Solution:
    def minOperations(self, nums):
        map = Counter(nums) # set up a dict to keep track of each number in nums and its occurance time

        count = 0 # variable to count operations needed

        for t in map.values(): # loop through the values in map
            if t == 1: # if the occurance of th number is one then return -1 as its not divisible by 2 or 3
                return -1
            count += t // 3 # add to count the number of times t is divisible by 3
            if t % 3: # if t is a modulo of 3 then add the one extra operation
                count += 1
        
        return count