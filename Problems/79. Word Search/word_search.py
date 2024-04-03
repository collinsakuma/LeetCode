from collections import Counter

class Solution:
    def exist(self, board, word):
        # create a dictionary using Counter to track all Letters in the 2D matrix and how many times each letter appears
        count = Counter(sum(board, []))

        # Check if the board consist of all of the letters in word
        for letter in set(word):
            # for a given letter in word if there are less instances of that letter in the board the word cannot be created, return False
            if count[letter] < word.count(letter):
                return False
        
        # for ease of traversal though the compare the count of the first and last leter of word
        # this will lessen the amount of starting points that need to be checked in order to find word in board
        if count[word[0]] > count[word[-1]]:
            # if there are more instances of the first letter than the last letter reverse the order of word
            word = word[::-1]

        # set variables for the count of columns, number or rows, and the length of word
        column = len(board)
        row = len(board[0])
        n = len(word)

        # depth-first search function
            # function variables
            # - i and j represent column and row 
            # - k represents word
            # - ind represets the index of the letter in word that is being searched for
        def dfs(i, j, k, ind):
            # if the end of the word has been reached then all letters in word have been found sucessfuly
            if ind == n:
                return 1
            # check if the coordinates being search are in the bounds of board
            if i < 0 or i >= column or j < 0 or j >= row:
                return 0
            # if board[i][j] returns -1 then this coordinates letter has already been used
            if board[i][j] == -1:
                return 0
            # if letter at the coordinate searched is not the letter, return False
            if k[ind] != board[i][j]:
                return 0
            
            # preserve the current cell being visiteds value
            temp = board[i][j]
            # mark that cell as visited ( already used )
            board[i][j] = -1 

            # set place holder values for the top, bottom, left, and right
            # to be used to check the coordinates around board[i][j]
            top = bottom = left = right = 0

            # check if the bottom, left, right, and top are valid positions
            bottom = dfs(i + 1, j, k, ind + 1)
            right = dfs(i, j + 1, k, ind + 1)
            left = dfs(i, j - 1, k, ind + 1)
            top = dfs(i - 1, j, k, ind + 1)

            board[i][j] = temp # restore the value to board[i][j]

            # if any are valid next positions return it
            return left or right or bottom or top
        
        # list of coordinates of the first letter in word
        ind_arr = []

        for i in range(column):
            for j in range(row):
                if board[i][j] == word[0]:
                    ind_arr.append([i,j])

        # loop though list of starting coordinates and perform depth-first search
        for i in ind_arr:
            if dfs(i[0], i[1], word, 0):
                return 1
            
        return 0