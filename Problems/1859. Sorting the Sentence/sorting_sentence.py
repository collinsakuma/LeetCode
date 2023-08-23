class Solution:
    def sortSentence(self, s):
        s_list = s.split(" ") # split s into an array separated at the spaces
        s_list.sort(key = lambda x: x[-1]) # sort the list by the number at the end of each word
        for i in range(len(s_list)): # loop though range of s_list
            s_list[i] = s_list[i][:-1] # remove the number from the end of each word in the list
        return " ".join(s_list) # rejoin the list into a string with spaces separating the words