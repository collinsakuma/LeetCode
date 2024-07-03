class Solution:
    def minDifference(self, nums):
        # if there are 4 or less numbers in the list then all numbers can be made the same
        # in three turns
        if len(nums) <= 4:
            return 0
        
        # sort the list of numbers
        nums.sort()

        #find the minumum that can be achieved between the three smallest and three largest numbers
        return min(nums[-1], nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])