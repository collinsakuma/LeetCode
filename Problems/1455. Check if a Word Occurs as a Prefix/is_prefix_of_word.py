class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        sentence_arr = sentence.split(" ") # split sentence string into a list of the words in the sentence

        for i in range(len(sentence_arr)): # loop though a range of length sentence_arr
            if searchWord == sentence_arr[i][:len(searchWord)]: # for each word in the sentence_arr compare the amount of letters equal to the search prefix to the searchWord to see if they are the same
                return i + 1 # if they are equal return the index of the word plus 1 (because of 0 indexing)
        return -1 # if none match return -1
    

    # second solution using build in function enumerate() 
    # 12/2/2024 question of the day came up with same solution
    # same basic idea of how to solve problem just a build in instaed of range
    def isPrefixOfWordTwo(self, sentence, searchWord):
        sentence_arr = sentence.split(" ")

        for i, word in enumerate(sentence_arr):
            if searchWord == word[:len(searchWord)]:
                return i + 1
        return -1