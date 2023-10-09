import Math

class Solution:
    def findRestaurant(self, list1, list2):
        output = [] # words in both list with the min index sum
        index_sum = Math.inf # set index sum initial value to infinity

        for word in list1: # loop through each word in list1
            if word in list2: # if the word is also in list 2 the find the index sum 
                # check if a new lowest index sum of the two words has been found 
                if list1.index(word) + list2.index(word) < index_sum:
                    # if new lowest index_sum 
                    # empty output list, as any word that was in the list is no longer the lowest index sum and must be deleted
                    # add the word into the new empty output list
                    # set new lowest index_sum
                    index_sum = list1.index(word) + list2.index(word)
                    output = []
                    output.append(word)
                    # if the sum of the two indexes for the word in both list is the same as the current lowest index_sum, append the word to the output, as it is also a valid min index sum
                elif list1.index(word) + list2.index(word) == index_sum:
                    output.append(word)
        return output # return the word(s) with the lowest index sum in the two list