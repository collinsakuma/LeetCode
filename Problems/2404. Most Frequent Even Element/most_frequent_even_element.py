class Solution:
    def mostFrequentEven(self, nums):
        # set empty variables to keep track of the highest frequency of any number and the actual number
        freq = number = 0
        set_sorted = sorted(set(nums)) # create a version of nums that is sorted and a set of unique numbers

        for num in set_sorted: # loop though list
            if num % 2 == 0: # check if the number is even
                if nums.count(num) > freq: # find the count of the num in nums if the count is greater than the current highest frequency
                    # set a new freq number and set number to num
                    freq = nums.count(num)
                    number = num
        
        if freq == 0: # if freq equals 0 then there is no number that appears more than once return -1
            return -1 
        else: # return the even number that occurs the most frequenctly, and or is the smallest number that appears freq amount of times
            return number