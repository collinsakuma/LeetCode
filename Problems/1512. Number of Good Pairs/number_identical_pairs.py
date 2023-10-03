class Solution:
    def numIdenticalPairs(self, nums):
        pairs = 0 # count the number of valid pairs found

        for i in range(len(nums) - 1): # loop though range of length nums
            # second loop for a list of nums at i to end of nums
            for j in nums[i + 1:]:
                # if num at i is the same as j then a valid pair has been found increment pairs
                if nums[i] == j:
                    pairs += 1
        return pairs # return number of pairs found