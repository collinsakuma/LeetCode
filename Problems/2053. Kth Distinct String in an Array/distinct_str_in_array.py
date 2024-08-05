from collections import Counter

class Solution:
    def kthDistinct(self, arr, k ):
        output = [] # list of strings that only appear once

        for string in arr: # loop though list of strings
            if arr.count(string) == 1: # if string only appears in arr once
                output.append(string) # add that string to the output list
        
        if len(output) < k: # if the amout of unique strings in arr is less than k return an empty string
            return ""
        else:
            return output[k - 1] # minus 1 from k to account for the 0 index
        

    def kthDistinctTwo(self, arr, k):
        count = Counter(arr) # create a counter dict
        # use a list comprehension to create a list of letters that have an occurance of only 1
        distinct_list = [i[0] for i in count.items() if i[1] == 1]

        # if the list of distinct characters is less than k return an empty string
        if len(distinct_list) < k:
            return ''
        else: # else return the kth distinct character
            return distinct_list[k - 1]
