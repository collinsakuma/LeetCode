class Solution:
    def maxNumberOfBalloons(self, text):
        # return the minimum value of using the .count() method for each letter in "balloon"
        # if a letter has no occurances in the text string 0 will be returned as you cannot make balloon with the letters given
        # for letters "l" and "o" divide by 2 and return the absoulte number becuase each letter occurs twice in balloon
        return min(text.count("b"), text.count("a"), text.count("l")//2, text.count("o")//2, text.count("n"))