class Solution:
    def thousandSeparator(self, n):
        n = str(n) # convert number n into a string
        n = n[::-1] # reverse the order of the numbers in n

        # create a new string 
        # - join the string with "." at inverals of 3
        new_n = ".".join(n[i:i + 3] for i in range(0, len(n), 3))

        return new_n[::-1] # return string new_n again reversing the order of the string again so its in the correct order.