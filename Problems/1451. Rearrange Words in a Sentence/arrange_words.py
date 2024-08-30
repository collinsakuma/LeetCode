class Solution:
    def arrangeWords(self, text):
        # create a matrix of words and its original order in the string
        word_matrix = []

        # loop through the words in the string, while tracking the index
        for idx, word in enumerate(text.split(' ')):
            # create a arr with the word in lower case letters with its index in the original string
            word_matrix.append([word.lower(), idx])

        # sort the words in the matrix by the length of the word in asscending order
        word_matrix.sort(key=lambda x:len(x[0]))
        # create a list of only the words 
        word_matrix = [word[0] for word in word_matrix]
        # join the list into a string
        word_matrix = ' '.join(word_matrix)

        # return the string capitalizing the first letter
        return word_matrix.capitalize()