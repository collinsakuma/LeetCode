from math import sqrt

class Solution:
    def bulbSwitch(self, n):
        return int(sqrt(n))
    

# n = 10
# r1  1 1 1 1 1 1 1 1 1 1
# r2  1 0 1 0 1 0 1 0 1 0
# r3  1 0 0 0 1 1 1 0 0 0
# r4  1 0 0 1 1 1 1 1 0 0
# r5  1 0 0 1 0 1 1 1 0 1
# r6  1 0 0 1 0 0 1 1 0 1
# r7  1 0 0 1 0 0 0 1 0 1
# r8  1 0 0 1 0 0 0 0 0 1
# r9  1 0 0 1 0 0 0 0 1 1
# r10 1 0 0 1 0 0 0 0 1 0

# only bulbs that can be squarerooted remain on bulb 1, 4, & 9