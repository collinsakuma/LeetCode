class Solution:
    def threeConsecutiveOdds(self, arr):
        for i in range(len(arr) - 2): # loop through the range of length of the array minus 2, minus two because there must be 3 consecutive odds
            if arr[i] % 2 != 0: # check if number at i index is odd
                # if number at index i is odd check if the next two numbers in sequence are also odd
                if arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                    return True # if both are odd return True as a sequence of three odd numbers has been found
        return False
    
    def threeConsecutiveOddsTwo(self, arr):
        count_odd = 0 # count of consecutive odd numbers

        # loop through numbers in the list
        for num in arr:
            # if number is odd increment the count of consecutive odds
            if num % 2 != 0:
                count_odd += 1
            # if number is even reset the count of consecutive odd numbers
            else:
                count_odd = 0
            # if three consecutive odds found return True
            if count_odd == 3:
                return True
        
        # return False if no three consecutive odds found
        return False