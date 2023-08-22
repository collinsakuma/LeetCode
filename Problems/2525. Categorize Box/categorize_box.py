class Solution:
    def categorizeBox(self, length, width, height, mass):
        # set two values of bulky and heavy to False initially
        bulky = False
        heavy = False

        # check conditions for if item is considered bulky 
        if length >= (10**4) or width >= (10**4) or height >= (10**4) or (length * width * height) >= (10**9):
            bulky = True # if any of the conditions are met set bulky to True
        # check conditions for if item is considered heavy
        if mass >= 100: 
            heavy = True # if mass of item is greater than or equal to 100 set heavy to True

        if bulky and heavy: # if bulky and heavy both true return Both
            return "Both"
        elif bulky: # if bulky is only true return bulky
            return "Bulky"
        elif heavy: # if heavy is only true return heavy
            return "Heavy"
        else: # if neither bulky or heavy is true return neither
            return "Neither"