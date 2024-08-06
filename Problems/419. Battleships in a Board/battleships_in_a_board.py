class Solution:
    def countBattleships(self, board):
        # save count of rows an columns to variables
        rows, columns = len(board), len(board[0])
        num_battleships = 0 # initalize the count of battleships

        # dfs function to recursivly find the battleships
        def find_battleships(row, column):
            # check if coordinates are inbound
            if row >= 0 and row <= rows - 1 and column >= 0 and column <= columns - 1:
                # check if coordinate is part of a battleship
                if board[row][column] != 'X':
                    return None
                else: # if coordinate is part of a battleship
                    # mark coordinate as visited
                    board[row][column] = ''
                    # recursiely check the surrounding coordinates for if they are part of the battleship
                    find_battleships(row - 1, column)
                    find_battleships(row + 1, column)
                    find_battleships(row, column - 1)
                    find_battleships(row, column + 1)
                    # return true if a battleship has been found
                    return True
            else:
                None

        # loop through all coordinates on the board
        for row in range(rows):
            for column in range(columns):
                # if a battleship is found increment battleship count
                if find_battleships(row, column):
                    num_battleships += 1

        return num_battleships