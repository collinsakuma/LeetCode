class Solution:
    def calPoints(self, operations):
        output = []

        for op in operations: # loop through each operation in operations
            if op.strip("-").isnumeric():
                # use the .strip() method to first remove any "-" from the op if its a negative number
                # next check if op is a number using the .isnumeric() method
                output.append(int(op)) # if it is a number append that op to the output list
            elif op == "+":
                # if op is a "+" add the two last numbers in the output list and append the sum
                output.append(int(output[-1]) + int(output[-2]))
            elif op == "D":
                # if the op is a "D" double the last index in the output list and append it
                output.append(int(output[-1]) * 2)
            elif op == "C":
                # if op is "C" remove the last score from the output list
                output.pop(-1)

        return sum(output) # return the sum of all of the scores in the output list
    