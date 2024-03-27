class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # min number will always be in range [1...n]
        for i in range(n):
            # if element is less than 1 or greater than the length of n
            if nums[i] < 1 or nums[i] > n:
                # set nums[i] in the range of 1 to n 
                nums[i] = n + 1

        for i in range(n):
            val = abs(nums[i])
            if val > n:
                continue
            val -= 1

            # flip nums value to negative to flag number
            if nums[val] > 0:
                nums[val] = -1 * nums[val]

        # return the first occurance of the non-negative number in the list
        for i in range(n):
            if nums[i] >= 0:
                return (i + 1)
            
        return n + 1