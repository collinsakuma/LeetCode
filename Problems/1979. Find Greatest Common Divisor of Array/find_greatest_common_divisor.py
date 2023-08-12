class Solution:
    def findGDC(self, nums):
        sorted_nums = sorted(nums) # sort nums
        lowest = sorted_nums[0] # get value of the smallest number in nums

        while lowest > 0: # while lowest is greater than 0 continue to loop
            # check if first first and last number in sorted_nums is divisible by the current lowest value
            if sorted_nums[0] % lowest == 0 and sorted_nums[-1] % lowest == 0:
                return lowest # return the lowest variable if true
            else:
                lowest -= 1
        return 1 # else return 1