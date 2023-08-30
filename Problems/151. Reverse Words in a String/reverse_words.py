class Solution:
    def reverseWords(self, s):
        s = s.split(" ") # turn the string s into a list that is split between the space " "
        while "" in s: # while there are empty strings in the list s "" 
            s.remove("") # remove those empty strings from the list

        return " ".join(s[::-1]) #reverse the list and join it as a string with space between the indexes