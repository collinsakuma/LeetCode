class Solution:
    def isCircularSentence(self, sentence):
        sentence_arr = sentence.split(" ") # turn the string into an array of words split at the spaces
        if len(sentence_arr) == 1: # first check if the string is only one word
            if sentence_arr[0][0] == sentence_arr[0][-1]:
                # if it is one word long check if the first letter and the last letter are the same
                return True # if true then it is a circular sentence
            return False
        
        # if the string is more that one word long second if statement is run
        if sentence_arr[0][0] == sentence_arr[-1][-1]:
            # check if the first letter of the first word in the list is the same as the last letter of the last word in the list
            for i in range(len(sentence_arr) - 1):
                if sentence_arr[i][-1] != sentence_arr[(i +1)][0]:
                    # compare the last letter of the word to the first letter of the next word if true continue checking if false return False
                    return False
            return True
        return False