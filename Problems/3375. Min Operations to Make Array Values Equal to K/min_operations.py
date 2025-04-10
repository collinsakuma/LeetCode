class Solution:
    def minOperations(self, nums, k):
        greater_k = 0 # count of numbers greater than k
        nums = set(nums) # set of unique numbers only

        # if theres is only 1 number in nums
        if len(nums) == 1:
            if list(nums)[0] == k: # check if num is the same value as k if same value no operatinons necessary
                return 0
            
        # loop through numbers
        for num in nums:
            # if num is greater than k increment greater_k
            if num > k:
                greater_k += 1
            # if any number is less than k then array cannot become equal with k
            elif num < k:
                return -1
            
        # if there are no numbers greater than k then array cannot become equal with k return -1
        if not greater_k:
            return -1
        else:
            # return number of operations necessary
            return greater_k