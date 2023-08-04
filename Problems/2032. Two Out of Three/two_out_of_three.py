class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        all_nums = set(nums1[:] + nums2[:] + nums3[:]) # create list of all numbers and then a set of the unique numbers excluding duplicates
        output = [] # set a empty list to append numbers that occurn in at least 2 of the list
        for num in all_nums: # loop though set of unique numbers
            count = 0 # set a count variable to keep track of how many list each num occurs in
            # check all three list checking if the current number occurs in each list and increase count by 1 if num is in list
            if num in nums1:
                count += 1
            if num in nums2:
                count += 1
            if num in nums3:
                count += 1
            if count >= 2: # if count is greater than or equal to 2 then num meets the requirements
                output.append(num) # append num to the output list
        
        return output