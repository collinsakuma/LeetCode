class Solution:
    def findTheWinner(self, n, k):
        # create a list of the friends playing the game
        nums =  list(range(n))

        i = 0 # set the initial person who starts the game

        # while there are more than 1 person left continue the game
        while len(nums) > 1:
            # find the person that will be eliminated from the game
            i = (i + k - 1) % len(nums)
            # remove the person at index i
            nums.pop(i)
        
        return nums[0] + 1