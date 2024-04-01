class Solution:
    def getWinner(self, arr, k):
        wins = 0 # count consecutive wins
        if len(arr) < k: # if the length of the arr is less than number of wins needed, return the largest number
            return max(arr)
        while wins < k: # start a loop that loops while the count of wins is less than wins
            if arr[0] > arr[1]: # if first number is greater than second
                wins += 1 #incresae wins by 1 
                loser = arr.pop(1) # pop the loser 
                arr.append(loser) # append the loser to the end of the array
            else: # if second number is greater than first
                # set new winner and append the loser to the end of the array
                wins = 1
                loser = arr.pop(0)
                arr.append(loser)
        return arr[0] # return the winner
    

    def getWinnerTwo(self, arr, k):
        count = 0 # count of consecutive wins
        winner = arr[0] # winner will always be the person first in the list
        
        for i in range(1, len(arr)): # loop through a range of all competing numbers to winner
            if arr[i] > winner: # if value at i is greater than winner set new winner
                winner = arr[i]
                count = 1 # reset count of consecutive wins to 1
            else:
                count += 1 # current winner remains the same increase their count of wins by 1
            
            if count == k: # if number of consecutive wins reaches the win condition k, return the winner 
                return winner
            
    def getWinnerThree(self, arr, k):
        # edge case where all players will play, return the highest player 
        if k >= len(arr):
            return max(arr)

        wins = 0 # keep count of wins
        # initalize player_1 and player_2 with the first two people in the list
        player_1 = arr.pop(0)
        player_2 = arr.pop(0)

        # loop untill k number of wins has been reached
        while wins < k:
            # if player 1 wins 
            if player_1 > player_2:
                wins += 1 # increment wins
                arr.append(player_2) # move player 2 to the end of the list
                player_2 = arr.pop(0) # set new player 2

            else:
                # if player 2 wins
                wins = 1 # reset wins to 1
                arr.append(player_1) # move player 1 to the end of the list
                player_1 = player_2 # make player 2 player 1
                player_2 = arr.pop(0) # set new player 2
        
        return player_1 # return the player who has achieved k numbers of wins