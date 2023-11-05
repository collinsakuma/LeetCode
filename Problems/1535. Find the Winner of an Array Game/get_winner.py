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