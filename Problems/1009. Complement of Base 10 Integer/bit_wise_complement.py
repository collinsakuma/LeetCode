class Solution:
    def bitwiseComplement(self, n):
        reverse = '' # set reverse to an empty string

        # only loop through binary of n from the second integer
        # bin(10) equal 0b101 so you only want to loop over 101 ignore '0b'
        for i in bin(n)[2:]:
            # reverse bits
            if i == 'i':
                reverse += '0'
            else:
                reverse += '1'
        # convert the bitwise back into an integer
        return int(reverse,2)
    