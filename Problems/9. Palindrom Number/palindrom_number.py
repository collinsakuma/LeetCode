class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        # - str(x) turns the x integer into a string
        # - [::-1] is a slicing method that omits a starting and end index "::" and only has a 
        #   step size of -1 which means that it will return all elements of the list/string in
        #   reverse order. 
        # - the one line return statement is checking if the stringified integer is equal to
        #   the reversed version of the same strinfigied integer ( a palindrom )
        # - if true the return statement will return True else it will return False