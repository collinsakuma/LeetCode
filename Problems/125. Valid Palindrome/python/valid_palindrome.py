class Solution:
    def isPalindrome(self, s):
        s = [i for i in s.lower() if i.isalnum()]
        # - simplify the string input into the function
        # - s.lower() makes all the letters in the string lower case
        # - if i.isalnum() will check all indexes of the string if they are a letter or a number
        #   if the index is either is will not add it to the new string.
        # - if the original value for s = "A man, a plan, a canal: Panama"
        #   the initial loop with mutate the string into s = "amanaplanacanalpanama"
        return s == s[::-1]
        # compare the reformated string s with the reverse of that.
        # s[::-1] reverses a string.