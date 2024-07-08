class Solution:
    def countFairPairs(self, nums, lower, upper):
        # count the number of pairs that are less than a certain value
        def count(n):
            output, j = 0, len(nums) - 1
            for i in range(len(nums)):
                while i < j and nums[i] + nums[j] > n:
                    j -= 1
                output += max(0, j - i)

            return output
        
        nums.sort()

        return count(upper) - count(lower - 1)
    