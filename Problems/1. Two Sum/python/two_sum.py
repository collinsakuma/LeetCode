

class Solution:
    def twoSum(self, nums, target):
        dict = {}  # initalized with an empty dictionary
        for i, n in enumerate(nums):
            #  enumerate loops through the list of numbers while keeping track of the index at i and the value at n.
            if n in dict:
                #  looking if n is in the dictionary meaning that it has found a complement whos sum = the target. 
                return [dict[n], i]
            else:
                dict[target-n] = i
                #  if no match is found a new entry to the dictionary is added (target - n): i
