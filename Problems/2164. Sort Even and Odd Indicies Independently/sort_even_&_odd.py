class Solution:
    def sortEvenOdd(self, nums):
        odds = [] # create a list of all numbers at odd indicies
        evens = [] # create a list of all numbers at even indicies
        final = [] # list to add sorted odd and even indicies too
        for i in range(len(nums)): # loop though range of length nums and add the indicies to the proper list (odds or evens)
            if i % 2 == 0: # if index is even append to evens list
                evens.append(nums[i])
            else: # if index is odd append to odds list
                odds.append(nums[i])

        odds.sort() # sort odds list
        evens.sort() # sort evens list
        odds = odds[::-1] # revserse the order of the odds list so it is in decreasing order
        shortest_list = min(len(odds), len(evens)) # set a variable for the shortest of the two lists ( more odd or even indicies)

        for i in range(shortest_list): # loop though the length of the sorter list
            final.append(evens[i]) # append the even index first so even indexes will increase in value
            final.append(odds[i]) # append the odd index next so odds will increment in a decreasing manner
        if len(evens) == shortest_list: # if the evens list is the shorter of the two list then append the remaining indexes of the odd list
            final += odds[shortest_list:]
        else: # if the odd list is the shorter one append the remaining even indexes
            final += evens[shortest_list:]
        return final # return the final sorted list