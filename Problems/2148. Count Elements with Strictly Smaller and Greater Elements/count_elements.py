class Solution:
    def countElements(self, nums):
        output = 0
        ordered = sorted(list(set(nums))) # create a set of nums, convert set to a list, then sort that list

        for num in nums: # loop though nums
            # find index of num in ordered, if index is greater than 0 and less than the lenght of ordered - 1 ( account for 0 index ) then there are smaller and larger number than num in list
            if ordered.index(num) > 0 and ordered.index(num) < len(ordered) - 1:
                output += 1 # increase output count by 1

        return output