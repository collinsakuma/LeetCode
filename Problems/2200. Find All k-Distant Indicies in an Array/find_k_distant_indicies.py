class Solution:
    def findKDistantIndicies(self, nums, key, k):
        index_j = [] # array of the indexes of numbers in nums that are equal to key

        # loop though nums if element is equal to key add its index to the index_j array
        for index, element in enumerate(nums):
            if element == key:
                index_j.append(index)

        output = [] # list of indexes that meet conditions

        for i in range(len(nums)): # loop though range of numbers
            for j in index_j: # second loop of indexes
                if abs(i - j) <= k: # check condition
                    output.append(i) # if condition met add index to output array, and break out the instance of the loop
                    break
        
        return sorted(output) # sort the list and return it