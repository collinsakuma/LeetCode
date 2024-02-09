class Solution:
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        nums.sort() # sort numbers
        res = [[num] for num in nums] # create sets starting with each number

        for i in range(n):
            for j in range(i):
                # check if nums are divisible by each other
                # second condition checks for max length subsets
                if nums[i] % nums[j] == 0 and len(res[i]) < len(res[j]) + 1:
                    res[i] = res[j] + [nums[i]]
        
        return max(res, key=len) # return the longest subset