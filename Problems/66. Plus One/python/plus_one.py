class Solution:
    def plusOne(self, digits):
        new_val = str(int(''.join(map(str, digits))) + 1)
        # map(str, digits) turnes all elements in the digits list into strings
        # ''.join() joins all elements in the list into a string
        # int() converts the newly formed string into an integer
        return [int(x) for x in new_val]