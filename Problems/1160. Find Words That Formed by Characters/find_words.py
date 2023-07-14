class Solution:
    def countCharacters(self, words, chars):
        answer = 0 # set answer varialbe to keep track of words that can be created with letters in chars

        for word in words: # loop though the words in words
            flag = True # set a flag variable to True if the word can be created with chars
            for letter in word: # loop though the letters in each word
                if chars.count(letter) < word.count(letter): # count the amount of times each letter is in chars and word
                    flag = False # if the count of letter is less in chars than in word set the flag to False (false meaning that the word cannot be produced by the letters in chars)
            
            if flag: # if flag (if flag = True)
                answer += len(word) # then add the len of word to answer
        
        return answer # return the answer