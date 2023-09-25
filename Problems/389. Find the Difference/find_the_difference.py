class Solution:
    def findTheDifference(self, s, t):
        for i in t:
            # check if the letter is in s
            if i not in s:
                return i
            # check if there are more instances of the letter in t than in s, if there are more of a letter in t than in s then return the letter
            if t.count(i) > s.count(i):
                return i
            