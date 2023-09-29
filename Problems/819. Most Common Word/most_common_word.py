class Solution:
    def mostCommonWOrd(self, paragraph, banned):
        chars = ["!","?","'",",",";","."] # characters of symbols that can be in the string paragraph
        non_banned_words = {} # empty dict to keep track of words in paragraph that arnt banned and their count of times they appear in paragraph

        for i in paragraph: # loop though each character in paragraph
            if i in chars: # if the characters is a symbol in chars, replace the character with a space
                paragraph = paragraph.replace(i, " ")
        paragraph = paragraph.split(" ") # turn the string into a list that is split at each space(" ")

        for word in paragraph: # loop through the list of words
            if not word: # if word is an empty string( i.e. a space ) do nothing, dont add to the dict
                None
            elif word.lower() not in banned: # change word to make sure its all in lower case letters, then check if it is a banned word
                if word.lower() not in non_banned_words: # if word isnt banned add isnt in the non_banned_words dictionary already
                    non_banned_words[word.lower()] = 1 # create new dict entry with the word as the key in lower case and a value of 1
                else: # if word is already in non_banned_words, increment that instance by 1
                    non_banned_words[word.lower()] += 1

        return sorted(non_banned_words.items(), key = lambda x:x[1])[-1][0]
        # for the return statement, breakdown as follows:
        # - sort the non_banned_words dictionary by the entire .item(), using the second index( the value ) as the key
        # - after the dictionary has been sorted return the last item [-1] and return only the key value [0]