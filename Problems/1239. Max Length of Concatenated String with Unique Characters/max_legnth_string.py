class Solution:
    def maxLength(self, arr):
        unique_elm = [''] # list of the unique concatenation of strings found
        maximum = 0 # max length of any unique string

        for i in range(len(arr)): # loop though the range of the length of the list
            # save the length of the list of unique strings to a variable
            size = len(unique_elm)
            # start a second loop to loop though the range of the length of unique_elm
            for j in range(size):
                # try all combinatins of strings in arr and unique strings in unique_elm
                concat = arr[i] + unique_elm[j]
                # check if the string has only unique elements by comparing its length to its set() length
                if len(concat) == len(set(concat)):
                    unique_elm.append(concat) # if the string is unique append it to the list unique_elm
                    maximum = max(maximum, len(concat)) # check if there is a new longest string using max()

        return maximum # return the length of the longest unique concatenated string