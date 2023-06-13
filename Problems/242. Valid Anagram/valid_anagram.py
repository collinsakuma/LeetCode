class Solution:
    def isAnagram(self, s, t):
        if len(s) < len(t): # first check if s has enough letter to even create an anagram for t
            return False
            # if len(t) is > len(s) then the letters in s cannot make an anagram of t returning False
        for letter in s:
            if s.count(letter) != t.count(letter):
            # for each letter in s count the amount of times that letter occurs and compare it to the count of that same letter in t
            # if the count is not the same then an anagram cannot be created
                return False
        return True