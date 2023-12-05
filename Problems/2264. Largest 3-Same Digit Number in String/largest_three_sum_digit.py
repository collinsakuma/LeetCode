class Solution:
    def largestGoodInteger(self, num):
        # list of all possible three digit combos
        three_digits = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]

        for combo in three_digits: # loop though all possible three digit combos
            if combo in num: # if the combo is the num string then return the three digit combo
                return combo
        
        return "" # if no combo appears in num string return an empty string