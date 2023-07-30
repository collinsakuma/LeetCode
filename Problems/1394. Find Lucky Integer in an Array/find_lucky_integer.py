class Solution:
    def findLucky(self, arr):
        sorted_backwards_set = sorted(set(arr))[::-1] # create a list of unique numbers in arr that is sorted in decending order

        for num in sorted_backwards_set: # loop though the numbers in sorted_backwards_set
            if num == arr.count(num): # if num is equal to the number of times that number appears in arr
                return num # return that number
        return -1 # if no number meets conditions return -1