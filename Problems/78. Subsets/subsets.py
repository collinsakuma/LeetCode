class Solution:
    def subsets(self, nums):
        output = [[]] # initialize list with one empty list, becuase all solutions will have []

        for i in nums: # loop through each num in nums
            output += [j + [i] for j in output] # append to output a new list comprehension that iterates over every element in output and appends i to it
            # example subsets(nums = [1,2,3]):
            # for i = 1 output += [[1]] because output only has one value to start with []
            # output now = [[], [1]]
            # for i = 2 output += [[2], [1,2]] because output now consist of 2 list [[], [1]] and appending 2 to those list gives you [2] and [1,2] which are both appended to the output list of list
            # output now = [[], [1], [2], [1,2]]
            # for i = 3 output += [[3], [1,3], [2,3], [1,2,3]]
            # output now = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
        return output