class Solution:
    def replaceElements(self, arr):
        greatest = arr[-1] # set the greatest current number to the last element in the array
        arr[-1] = -1 # set the last element in the array to -1

        for i in range(len(arr) - 2, -1, -1): # loop though the list backwards skipping the last index
            cur = arr[i] # set a temp variable to current element
            arr[i] = greatest # set element at index i to the greatest number to its right
            if greatest < cur: # if current greatest number is less than current number at index i replace greatest
                greatest = cur
        return arr # return array