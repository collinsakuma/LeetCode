class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        # find the difference between how many candies alice and bob have
        candy_diff = (sum(aliceSizes) - sum(bobSizes)) / 2

        aliceSizes = set(aliceSizes) # Change alice's sizes to only unique numbers
        for candy in set(bobSizes): # loop though each sizes of bobs bags but only unique sizes
            if candy_diff + candy in aliceSizes: # if the candy difference plus the candy instance of bob is in Alice's sizes then there can be a like for like exhange of the two bags
                return [candy_diff + candy, candy]