class Solution:
    def decodeMessage(self, key, message):
        key_string = "".join(key.split(" ")) # create a new key string without the spaces
        # create a dictionary to keep the values of the key with a coresponding letter it represents
        # dict has a starting value of " ":" " to represent spaces, that do not have coded value
        dict = {" " : " ",} 
        abc = 1 # set a value of the keys, for each new key letter it must represent the next letter in the alphabet
        decode = "" # empty string to construct the decoded message

        for key in key_string: # loop though all variables in key_string
            if key not in dict: # if the letter does not exist in the dict
                # create a new dictionary entry for that letter with the corresponding letter in the aphabet starting at a-z
                dict[key] = chr(ord("`") + abc) # chr(ord("`") + abc) converts a number 1-26 to its alphabet equivalent
                abc += 1 # increment abc by 1
            else: # if the letter is already in dict, do nothing only the first occurance of the letter sets the key value
                None 
        
        for i in message: # loop though message and add the coded value to the decode string
            decode += dict[i]
        
        return decode # return the decoded message