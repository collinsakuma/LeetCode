class Solution:
    def intersection(self, nums):
        intersects = [] # empty list to hold numbers that are in all lists
        # create a list of numbers that will be checked if they are in all list
        # - take a set of the first list at index 0 then sort the set
        numbers = sorted(set(nums[0]))

        for i in numbers: # loop though each number in numbers
            flag = False # set a flag value initialy to false
            for j in range(1, len(nums)): # start a second loop from 1 to length numbers, skip 0 index because the set of numbers being checked is the 0 indexed list
                # check if the current number( i ) is in each list j
                if i not in nums[j]:
                    # if i is not in any of the list, set flag to True and break out of the current loop
                    flag = True
                    break
            if not flag: # check if flag is false, if flag is false then i is in all list, append to intersects list
                intersects.append(i)
        return intersects # return list of numbers that are in all list, or an empty list if no number is in all lists