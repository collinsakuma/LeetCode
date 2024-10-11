class Solution:
    def maxWidthRamp(self, nums):
        max_width = 0 # track max width

        # loop through range of numbers
        for i in range(len(nums)):
            # loop through the range of numbers left after i in reverse order
            for j in range(len(nums) - 1, i, -1):
                # if nums[i] <= nums[j] check for a new max width
                if nums[i] <= nums[j]:
                    # check for new max width
                    max_width = max(max_width, j - i)
                # if remaning widths are no wider than the current max, break from the loop ( do not check rest )
                if j - i < max_width:
                    break
        
        return max_width # return the max width