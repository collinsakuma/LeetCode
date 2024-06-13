class Solution:
    def sortColors(self, nums):
        # count how many 0,1,2 are in nums
        count_0 = nums.count(0)
        count_1 = nums.count(1)
        count_2 = nums.count(2)

        # loop through the indexes of nums
        for i in range(len(nums)):
            # first replace the indexes with 0's untill there are no more to replace
            if count_0:
                nums[i] = 0
                count_0 -= 1
            # next replace the indexes with 1's
            elif count_1:
                nums[i] = 1
                count_1 -= 1
            # lastly replace the remaning indexes with 2's
            else:
                nums[i] = 2