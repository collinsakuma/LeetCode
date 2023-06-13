class Solution:
    def firstUniqChar(self, s):
        for i, letter in enumerate(s):
            # use enumerate() method to loop through s while keeping track of what index is being iterated over
            if s.count(letter) == 1:
                # - want to find the first non-repeating character (I.E. it only occurs once in the string)
                # - so for each letter check if the count of that letter is equal to 1 if so they the first unique letter has been found
                #   return the index being tracked by the i variable. 
                return i   
        return -1
    

    # second solution, solving by creating a dictionary
    def firstUniqChar(self, s):
        dict = {} # create an empty dictionary to keep track of letters
        for letter in s:
            # for each letter in s if the letter is not in dict create a new entry to dict with the letter as the key and a starting value of 1
            if letter not in dict:
                dict[letter] = 1
            else:
                # if the letter is already in the dictionary increment its value by 1
                dict[letter] += 1
        
        index = -1
        # now check the entries of the dictionary to see if any keys have a value of 1
        # return the index of that value if found
        for i in range(len(s)):
            if dict[s[i]] == 1:
                index = i
                break
        return index

