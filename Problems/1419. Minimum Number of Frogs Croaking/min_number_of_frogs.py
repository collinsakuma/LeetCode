class Solution:
    def minNumberOfFrogs(self, croakOfFrogs):

        min_frogs = 0 # minimum number of frogs needed to croak

        # helper function to check if a croak has been completed
        def croak_finished(chars_dict):
            for value in chars_dict.values():
                if value < 1:
                    return False
            return True
        
        # dict for count of each letter in croak
        chars = {'c': 0, 'r': 0, 'o':0, 'a':0, 'k':0}

        # loop through string of croaks
        for ch in croakOfFrogs:
            # increase count of each character
            chars[ch] += 1

            # make sure that each character in croak does not have a greater value than the previous letter if so croak cannot be formed in order
            if chars['c'] < chars['r'] or chars['r'] < chars['o'] or chars['o'] < chars['a'] or chars['a'] < chars['k']:
                return -1
            
            # check for a new amount of frogs needed to croak
            min_frogs = max(min_frogs, chars['c'])

            # if a croak is finished remove one croak from the chars dict
            if croak_finished(chars):
                for i in 'croak':
                    chars[i] -= 1

        # check if there are left over characters in the chars dict, if there is then finished croaks cannot be made return -1
        if any(value > 0 for value in chars.values()):
            return -1
        
        else:
            return min_frogs