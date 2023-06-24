class Solution:
    def differenceOfSum(self, nums):
        
        element_sum = sum(nums) # find the sum of nums for the element sum
        digit_sum = 0 # create a variable for the digit sum and set equal to 0

        curr = '' #create a curr variable to store the num in string form during iteration

        for num in nums: # iterate through the nums list
            curr = str(num) # set curr to the current num being iterate on as a string
            for i in curr: # loop through the elements of the curr number
                digit_sum += int(i) # add each number in the curr string to digit_sum by converting it to an int first
        return element_sum - digit_sum # return the diff between element and digit sumit 