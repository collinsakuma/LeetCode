class Solution:
    def isHappy(self, n):
        visited = set()
        # keep track of numbers that have already been evaluated
        # if a number number in the set comes up the it is an infinite loop and is False

        while n != 1:
            sum_of_squares = 0

            # find sum of squares of digits in n
            while n > 0:
                digit = n % 10
                sum_of_squares += digit ** 2
                n //= 10
            
            # check if the sum is already in visited
            if sum_of_squares in visited:
                # if sum is in visited a infinit loop has been found return False
                return False

            # add sum to the visited set
            visited.add(sum_of_squares)

            # set n to be the sum of squares for the next iteration
            n = sum_of_squares
        
        return True