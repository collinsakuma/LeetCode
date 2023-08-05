class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        output = [True] * len(candies) # create a list equal length to candies will True as every index value

        for i in range(len(candies)): # loop though range of length candies
            if candies[i] + extraCandies < sorted(candies)[-1]: # if candies at index i is not greater than the most candies that any child has at the begining ( sorted index in assending order and the last index)
                output[i] = False # that means that child does not have the most candies of all set the output at index i to False
        return output