class Solution:
    def maxAscendingSum(self, nums):
        max_sum = 0 # value to keep track of max ascending sum reached
        temp_sum = nums[0] # set temp initially first number in nums

        # loop though range of numbers starting at the second index, (first index is intial value of temp_sum)
        for i in range(1, len(nums)):
            # if num[i] greater than previous number increase temp_sum count
            if nums[i] > nums[i - 1]:
                temp_sum += nums[i]
            # if num[i] less than prevous number ascending sum is no longer valid
            # check for a new max sum
            # then reset temp_sum initial value to nums[i]
            elif nums[i] < nums[i -1]:
                max_sum = max(max_sum, temp_sum)
                temp_sum = nums[i]
            # if nums[i] equal to previous number asending numbers is no longer valid
            # check for new max_sum
            # reset temp_sum to value of nums[i]
            elif nums[i] == nums[i - 1]:
                max_sum = max(max_sum, temp_sum)
                temp_sum = nums[i]
        return max(max_sum, temp_sum) # return either max_sum of temp_sum whichever is greater
    
    def maxAscendingSumTwo(self, nums):
        max_sum, cur_sum = 0, nums[0]

        for i in range(1, len(nums)):
            # if current number is greater than previous number
            if nums[i] > nums[i - 1]:
                # increment running sum
                cur_sum += nums[i]
            # if not assending
            else:
                # check if new max sum has been found
                max_sum = max(max_sum, cur_sum)
                # set new running sum to the current element
                cur_sum = nums[i]
        return max(max_sum, cur_sum)