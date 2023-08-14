class Solution:
    def minMoves(self, target, maxDoubles):
        count = 0 # keep track of the amount of moves that are made
        
        while target != 1: # while target is still greater than 1 continue to make moves ( loop )
            if target % 2 != 0: # if target is an odd number first make a move to make an even number before the maxDouble moves are made
                target -=1 # reduce the target by 1 ( move made )
                count += 1 # increase the moves made count by 1
            if maxDoubles > 0: # if there are max double moves to be made use them first
                target = target // 2 # divide target by 2 
                count += 1 # incresae moves made by 1
                maxDoubles -= 1 # decrease the amount of maxDouble moves remaining
            else: # after all maxDouble moves are used up the remainder must be reduced by increments of 1
                count += target - 1 # increase the count of moves needed by remainder of target - 1
                target -= target - 1
        return count # return the amount of moves made