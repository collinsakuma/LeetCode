class Solution:
    def reformat(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()] # create a list of the letters in s
        digits = [c for c in s if c.isdigit()] # create a list of the numbers in s
        if abs(len(letters) - len(digits)) > 1: # if the difference between the amount of letters and numbers is greater than 1 return an empty string
            return ""
        
        rv = []
        flag = len(letters) > len(digits)
        while letters or digits: # while there are still enteries in letters and digits continue the loop
            rv.append(letters.pop() if flag else digits.pop()) # alternate adding to the response list
            flag = not flag
        return rv # return the rearranged string