class Solution:
    def squareIsWhite(self, coordinates):
        if coordinates[0] in 'aceg': # check to see if the letter part of the coordinates is in the string of coordinates
            if int(coordinates[1]) % 2 != 0: # check if the number returns a remainder if it does the coordinate is a black square
                return False
            else:
                return True
        if int(coordinates[1]) % 2 != 0: # if the letter part of the coordinate is not in the string 'aceg'
            return True # if the coordinate number returns a remainder it is a white square and return True
        else:
            return False