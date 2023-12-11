from collections import Counter

class Solution:
    def findSpecialInteger(self, arr):
        num_required = len(arr) / 4 # find 25% of the length of the array
        for num in set(arr): # loop though unique set of numbers in arr
            # count the number of times that num appears in arr
            # if num apprears more than 25% of len(arr) return that number
            if arr.count(num) > num_required:
                return num
            
    def findSpecialIntegerTwo(self, arr):
        count = Counter(arr) # use counter to create a dictionary of each element as the key and its frequency as the value
        # return the most common 1 in count, item that appears the most frequently, [0] first object in dict, [0] first element in the object
        return count.most_common(1)[0][0]