class Solution:
    def findSpecialInteger(self, arr):
        num_required = len(arr) / 4 # find 25% of the length of the array
        for num in set(arr): # loop though unique set of numbers in arr
            # count the number of times that num appears in arr
            # if num apprears more than 25% of len(arr) return that number
            if arr.count(num) > num_required:
                return num