class Solution:
    def numberOfPairs(self, nums):
        pairs, leftovers = 0, 0 # variables to keep track of the number of pairs in nums and leftover numbers
        set_nums = set(nums) # create a set of unique numbers in nums

        for num in set_nums: # loop though the unique list of numbers
            count = nums.count(num) # set the count of how many times each num appers in nums
            if count >= 2: # if there is 2 or more occurances of num in nums
                pairs += count // 2 # add pairs of that number
                leftovers += count % 2 # then add the extra (odd) occurances
            else: # if there is only one occurance of num add it as an odd leftover number
                leftover += 1

        return [pairs, leftovers] # return the pairs and leftovers count