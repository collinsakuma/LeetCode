from collections import Counter

class Solution:
    def findOriginalArray(self, changed):
        if len(changed) % 2 != 0: # if the list of numbers isnt an even amount than there cannot be a dupliate array
            return [] # return an empty array
        
        changed.sort() # sort the list of numbers
        count = Counter(changed) # create a count dictionary that keeps track of how many times each number appears in the list
        answer = [] # create an empty list to add original numbers too

        for num in changed: # loop though the list of umbers
            if count[num] >= 1: # check how many times num occurs in the list
                count[num] -= 1 # if there is 1 or more occurance of the num reduce its count by 1
                if count[num * 2] >= 1: # check if there are instances of num * 2
                    count[num * 2] -= 1 # if instances exist reduce num * 2 count by 1
                    answer.append(num) # append the num to the answer list
                else:
                    return [] # if num * 2 does not exist return an empty list
                
        if len(answer) == len(changed)/2: # if the answer reaches a length of half the changed list the original list has been found
            return answer # return the list
        
        return []