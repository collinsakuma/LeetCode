class Solution:
    def uniqueOccurrences(self, arr):
        count = [] # list to hold the amount that letters occur in arr

        for i in set(arr): # loop though a list of unique elements in arr
            if arr.count(i) in count: # count how many times an element is in arr, if that count is already in the count list then the count is not unique, return False
                return False
            else: # if the count is unique, append that number to the count list
                count.append(arr.count(i))
        return True # if all elements are unique return True