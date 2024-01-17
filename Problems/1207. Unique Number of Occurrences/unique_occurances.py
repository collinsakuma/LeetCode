from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr):
        count = [] # list to hold the amount that letters occur in arr

        for i in set(arr): # loop though a list of unique elements in arr
            if arr.count(i) in count: # count how many times an element is in arr, if that count is already in the count list then the count is not unique, return False
                return False
            else: # if the count is unique, append that number to the count list
                count.append(arr.count(i))
        return True # if all elements are unique return True
    

    # second solution using build in method Counter()
    def uniqueOccurrencesTwo(self, arr):
        count = Counter(arr) # create a dictionary using the Counter() method to keep track of each element in the list and how many times each element is in the list
        # compare the length of a list of the values in the count dicitonary to the length of unique values of the same list
        # if the lengths are the same the each element occurs a unique number of times in the list
        # if the lengths are not the same the two or more elements share the same occurance frequency in the list
        return len(count.values()) == len(set(count.values()))