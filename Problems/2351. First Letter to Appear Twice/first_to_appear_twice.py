class Solution:
    def repeatedCharacter(self, s):
        dict = {} # create an empty dictionary to keep track of each letter as the key and how many times it has occured as the value
        
        for i in s: # loop though each letter in the string s
            if i not in dict: # if the letter is not already a key in the dict create a new key value pair with i as the key and 1 as the value
                dict[i] = 1
            else: # if i already a key in dict increment its value by 1
                dict[i] += 1
            
            if dict[i] == 2: # check if i has a value of 2 meaning that it has appeared twice in the string. If true return that letter
                return i
            

    # second solution with some redundant code removed
    def repeatedCharacterTwo(self, s):
        dict = {}

        for i in s:
            if i not in dict:
                dict[i] = 1
            else: # becuase we are only looking for the first letter to repeat twice if i already exist as a key in dict
                  # we can return that i because it will be the first letter that already has an entry in the dict meaning that it is appearing for the second time
                return i