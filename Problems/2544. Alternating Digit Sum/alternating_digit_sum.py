class Solution:
    def alternateDigitSum(self, n):
        sum = 0 # set sum variable to keep track of total sum as each number is added
        for i, j in enumerate(str(n)): # use enumerate to loop though each number in n, as well as keep track of the index value of each element
            if i % 2 == int(j): # if num j is at a even index, add j to sum as a positive integer
                sum += int(j)
            else: # if j is at a odd index, add j to sum as a negative number
                sum += int(j) * -1
        return sum # return sum after all number in n have been looped through