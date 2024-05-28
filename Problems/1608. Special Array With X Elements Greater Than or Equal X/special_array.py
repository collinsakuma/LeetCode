class Solution:
    def specialArray(self, nums):
        # sort array
        nums = sorted(nums)
        # loop though range of possible x values
        for x in range(0, len(nums) + 1):
            # set a count variable to track numbers in nums greater than or equal to x
            count = 0
            # loop through nums list
            for num in nums:
                # if number is greater than or equal to x increase count by 1
                if num >= x:
                    count += 1
                # if the count of numbers greater than x becomes more than x
                # break from the loop as this x value cannot be the special x
                if count > x:
                    break
            # if after looping through nums the count of numbers greater than or equal
            # to x is equal to x the special value has been found and return x
            if count == x:
                return x
            
        return -1 # no special x found