from collections import Counter

class Solution:
    def relativeSortArray(self, arr1, arr2):
        sorted_arr1 = []
        
        # use counter
        counter = Counter(arr1)

        # loop through numbers in the second key array
        for num in arr2:
            # if number in array 1
            if num in counter:
                # add it to the new sorted array the number of times that 
                # that it appears in arr1
                sorted_arr1 += [num] * counter[num]
                # set its count value to 0
                counter[num] = 0

        # loop through the items of the sorted counter
        for item in sorted(counter.items(), key=lambda x:x[0]):
            # if the items didnt appear in the key array add it to the new list
            if item[1] != 0:
                sorted_arr1 += [item[0] * item[1]]

        return sorted_arr1