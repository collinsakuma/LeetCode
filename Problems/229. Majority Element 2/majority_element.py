class Solution:
    def majorityElement(self, nums):
        occurance = len(nums) / 3 # find the desired occurance level
        output = [] # emtpy list to add numbers that appear in the list more times than the occurance level

        for num in set(nums): # loop though a unique list of nums
            if nums.count(num) > occurance: # use .count() to find how many times each num is in nums
                # if num appears more times than the value of occurance append num to the output list
                output.append(num)
        
        return output