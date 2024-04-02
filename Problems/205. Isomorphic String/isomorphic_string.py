class Solution:
    def isIsomorphic(self, s, t):
        # dict to hold letter and letter that it will be switched to
        mirror_dict = {}

        # if there is a difference in the unique characters in the strings
        # they cannot be isomorphic
        if len(set(s)) != len(set(t)):
            return False
        
        # loop though a range of the length of the string
        for i in range(len(s)):
            # if the letter at s[i] is already in the dict ( mirrored to another letter )
            if s[i] in mirror_dict:
                # if the letter t[i] doesnt match the letter s[i] is already beeing swapped with, return False
                if mirror_dict[s[i]] != t[i]:
                    return False
            # if s[i] not paired already with a letter in string t to replace, pair it with t[i] in mirror_dict
            else:
                mirror_dict[s[i]] = t[i]

        return True
    
    def isIsomorphicTwo(self, s, t):
        # two empty list to map the index value of the letters
        map_s = []
        map_t = []

        # loop through s
        for letter in s:
            # for each letter append the index that it appears first into map_s
            map_s.append(s.index(letter))
        
        for letter in t:
            # for each letter append the letter that it appears forst into map_t
            map_t.append(t.index(letter))
        
        if map_s == map_t: # if the two map arrays are the same the the string is isomorphic
            return True

        return False