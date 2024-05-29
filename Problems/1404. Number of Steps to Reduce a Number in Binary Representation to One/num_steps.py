class Solution:
    def numSteps(self, s):
        # conver the binary string into a number
        num_s = int(s, 2)
        # set a count for the amount of operations done to the number
        operation_count = 0
        # when the number isnt one continue the loop
        while num_s != 1:
            # if number is even divide by 2
            if num_s % 2 == 0:
                num_s //= 2
                operation_count += 1
            # if number is odd add 1 
            else:
                num_s += 1
                operation_count += 1
        return operation_count