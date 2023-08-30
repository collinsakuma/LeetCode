class Solution:
    def reverseWords(self, s):
        s = s.split(" ") # turn the string s into a list that is split between the space " "
        while "" in s: # while there are empty strings in the list s "" 
            s.remove("") # remove those empty strings from the list

        return " ".join(s[::-1]) #reverse the list and join it as a string with space between the indexes
    

    def reverseWordsTwo(self, s):
        word_list = [] # set empty list to hold words
        word = "" # set a word variable to an empty string

        for i in s: # loop though each variable in s
            if i != " ": # if i is not a space(" ")
                word += i # add the letter to the word
            elif word != "": # if i is a space and word isnt an empty string
                word_list.append(word) # append the word to the word_list
                word = "" # reset word to an empty string
        if word != "": # at the end of the string check if word isnt an empty string
            word_list.append(word) # if its not empty append the word to word_list

        return " ".join(word_list[::-1]) # join a reversed order word_list into a string with spaces between each element