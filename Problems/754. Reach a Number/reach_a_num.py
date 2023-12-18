class Solution:
    def reachNumber(self, target):
        target = abs(target) # if target is a negative or positive number of moves to get to it will be the symetical, so only focus on positive
        n, dist = 0, 0 # set n to keep track of number of moves made, dist to keep track of total traversed

        # start a loop and continue while dist is less than target number or until distance traveled minus target modulo 2 does not equal 0
        while dist < target or (dist - target) % 2 != 0:
            n += 1
            dist += n
        
        return n