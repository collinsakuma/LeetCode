class Solution:
    def numSmallerByFrequency(self, queries, words):
        output = [0] * len(queries) #return output equal in length to queries array set default values to 0


        # helper function 
        def f(s):
            # set two values for ltr to keep track of the lexicographically smallest letter
            # and count to track how many times the smallest letter apears in s
            ltr, count = 27, 0
            for letter in set(s): # loop though a set of letters in s
                if ord(letter) - 97 < ltr: # find the lexiconal vaule of letter and see if its a new lower value
                    # if it is lower, set a new lowest value of ltr, and the count of that letter in s
                    ltr = ord(letter) - 97
                    count = s.count(letter)
            return count # return the count of the smallest letters count in s
        
        # loop through the range of the length of queries
        for i in range(len(queries)):
            greater = 0 # keep a count of how many words have a greater value than the current query
            count = f(queries[i]) # find the count of the smallest character in the query using the helper fuction f(s)

            for word in words: # loop though the words list
                # compare the count of the smallest letter in word to count
                if f(word) > count:
                    greater += 1 # if the value is greater increase greater count by 1
            output[i] = greater # set the value of output[i] to the amount of words whose f(s) value was greater

        return output 