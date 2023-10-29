class Solution:
    def distributeCandies(self, candyType):
        n = len(candyType) / 2 # find the amound of candies Alice can eat
        types = set(candyType) # create a list of only unique candies

        if n <= len(types): # if n is equal to or less than the amount of unique candies, then every candy Alice can eat can be unique
            return int(n)
        else: # Alice can can eat more candies than there are unique candies, return the amount of unique candies
            return len(types)