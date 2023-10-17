class Solution:
    def threeConsecutiveOdds(self, arr):
        for i in range(len(arr) - 2): # loop through the range of length of the array minus 2, minus two because there must be 3 consecutive odds
            if arr[i] % 2 != 0: # check if number at i index is odd
                # if number at index i is odd check if the next two numbers in sequence are also odd
                if arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                    return True # if both are odd return True as a sequence of three odd numbers has been found
        return False