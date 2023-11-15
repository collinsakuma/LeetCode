from statistics import mean

class Solution:
    def trimMean(self, arr):
        arr = sorted(arr) # sort the arr

        remove_amount = len(arr) * (1/20) # determine how many elements need to be removed 5%

        # find the mean of the arr excluding the elements that are to be removed (lowest 5% of numbers and greatest 5% of numbers)
        return mean(arr[int(remove_amount):len(arr) - int(remove_amount)])