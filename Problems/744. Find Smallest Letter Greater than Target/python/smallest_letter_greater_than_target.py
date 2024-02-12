class Solution:
    def nextGreatestLetter(self, letters, target):
        # create a dict with all letters and associate a number value with each letter.
        alphabet = {
            "a":1,
            "b":2,
            "c":3,
            "d":4,
            "e":5,
            "f":6,
            "g":7,
            "h":8,
            "i":9,
            "j":10,
            "k":11,
            "l":12,
            "m":13,
            "n":14,
            "o":15,
            "p":16,
            "q":17,
            "r":18,
            "s":19,
            "t":20,
            "u":21,
            "v":22,
            "w":23,
            "x":24,
            "y":25,
            "z":26 
        }
        
        for i in letters:
        # for each letter in the list compare if its values in the alphabet dict is greater than that of the target value.
        # if the value is greater then the least smallest letter greater than the target has been found
        # because the letters list is ordered for us there is no need for more complex logic. The first match is the answer
            if alphabet[i] > alphabet[target]:
                return i
        return letters[0]
    

    # for this second solution a dictionary of letter: value pairs is not needed because python 
    # can compare the letters as it gives letters weighted values. I.E. (a < b = true)
    def nextGreatestLetterTwo(self, letters, target):
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]