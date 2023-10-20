import math

class Solution:
    def pickGifts(self, gifts, k):
        while k != 0: # while there are seconds left continue the operations
            gifts = sorted(gifts) # sort the gifts array
            # get the floor of the squared value of the largest pile in the array
            squared = math.floor(math.sqrt(gifts[-1]))
            gifts[-1] = squared # set the new amount of gifts left for the previously largest pile of gifts
            k -= 1 # reduce k by 1 as one second has passed
        return sum(gifts) # return the sum of the remaining gifts