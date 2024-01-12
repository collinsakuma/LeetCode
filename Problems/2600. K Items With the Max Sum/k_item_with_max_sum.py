class Solution:
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        num_list = [] # initalize a list to add all the 1, 0, -1
        # add the 1, 0, -1 's to the list
        num_list += ([1] * numOnes)
        num_list += ([0] * numZeros)
        num_list += ([-1] * numNegOnes)

        num_list = sorted(num_list) # sort the list of numbers

        # return the sum of the k last numbers in the list
        return sum(num_list[len(num_list) - k:])