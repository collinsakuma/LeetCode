class Solution:
    def findSubarrays(self, nums):
        seen = set() # keep track of unique sums
        for i in range(len(nums) - 1): # loop through range of length nums minus 1
            s = nums[i] + nums[i + 1] # find the sum of a pair
            if s in seen: # if the sum is in s then an equal sum has been found return True
                return True
            seen.add(s)

        return False # if no two sums are found return False