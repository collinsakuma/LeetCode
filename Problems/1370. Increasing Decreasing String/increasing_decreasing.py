class Solution:
    def sortString(self, s):
        s = list(s) # turn the sting s into a list
        answer = ""

        while s: # continue loop till s has no more letters
            for letter in sorted(set(s)): # in a sorted list of a set of s
                s.remove(letter) # remove the first letter
                answer += letter # append that letter to answer
            for letter in sorted(set(s), reverse=True): # in a sorted list of a set of s but reversed
                s.remove(letter) # remove the first letter
                answer += letter # append that letter to answer
        return answer
    