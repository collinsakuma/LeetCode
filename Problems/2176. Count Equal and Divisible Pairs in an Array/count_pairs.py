class Solution:
    def countPairs(self, nums, k):
        count = 0 # keep track of pairs that meet conditions
        for i in range(len(nums)): # loop through range of length nums
            for j in range(i + 1, len(nums)): # start a second loop that loop though range of nums from i
                if nums[i] == nums[j]: # check if number values of both indexes are the same
                    if (i * j) % k == 0: # if the same check if the indexes multiplied by eachother are divisors of k
                        count += 1 # if pair meet all coondtions increase count by 1
        return count