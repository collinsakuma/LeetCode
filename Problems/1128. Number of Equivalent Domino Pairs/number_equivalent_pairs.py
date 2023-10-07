class Solution:
    def numEquivDominoPairs(self, dominoes):
        dict = {} # set empty dictionary to keep track of domino pairs and their frequency

        for i in dominoes: # loop though all dominoes
            pair = tuple(sorted(i)) # set each domino to a sorted pair converted into a tuple
            if pair in dict: # if the pair is in the dictionary increment that entry by 1
                dict[pair] += 1
            else: # else create a new dictionary entry
                dict[pair] = 1
        
        count = 0 # set a count value 
        for j in dict.values(): # loop though the values in dict summing them up to return the count of pairs
            s = j * (j - 1) // 2
            count += s
        return count