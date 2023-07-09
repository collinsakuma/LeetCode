class Solution:
    def commonFactors(self, a, b):
        common = 1 # create a common factors variable with value of 1 because 1 will always be a common factor

        if a >= b: # if a is greater than or equal to b loop though only range a
            for i in range(2, a + 1):
                if a % i == 0 and b % i == 0: # if both a and b % i return 0 than i is a common factor 
                    common += 1
        else: # if b is greater than a only loop trough rance of b
            for i in range(2, b):
                if a % i == 0 and b % i == 0: # same as before if a and b % i return 0 than i is a common factor
                    common += 1
        return common # return the number of common factors