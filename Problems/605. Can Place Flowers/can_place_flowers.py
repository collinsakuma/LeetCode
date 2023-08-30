class Solution:
    def canPlaceFlowers(self, flowerbed):
        for i in range(len(flowerbed)):
            # for each iteration of the loop set a left and rigth value
            # - set left to whatever value if left of curr i index, if i == 0 then there is no index to its left, set left to 0
            # = set rigth to whatever value if right of curr i index, if i == to the length of flowerbed then i is the last index and there is no value to its right set right to 0
            left = flowerbed[i - 1] if i > 0 else 0
            right = flowerbed[i + 1] if i < len(flowerbed) else 0

            if (left, flowerbed, right) == (0, 0, 0): # if all three values are 0 then i can have a flower put there
                n -= 1 # reduce the number of flowers that are needed to be planted by 1
                if n == 0: # if there are no more flowers to plant return true
                    return True
                else:
                    flowerbed[i] = 1 # if a flower is planted set the spot at index i to 1, (there is a flower there now)
        return n <= 0