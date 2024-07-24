from collections import defaultdict

class Solution:
    def stoneGameIX(self, stones):
        frequency = defaultdict(int)

        for i in stones:
            frequency[i % 3] += 1
        # if there is a even number of stones whos modulo of 3 equal 0
        # if there are any number of stones whos modulo 3 equal 1 or 2
        # Alice will always win becuase bob will have to place the last 1 or 2 
        # giving Alice the iwn
        if frequency[0] % 2 == 0:
            return frequency[1] and frequency[2]
        
        # if there is an odd number of 0 frequency numbers then allice will need 
        # three or more numbers remaining to win
        return abs(frequency[1] - frequency[2]) >= 3
