from collections import Counter

class Solution:
    def longestPalindrome(self, s):
        # set variable to find the max length possible for a palindrome
        max_length = 0
        # create a dict using the Counter() method
        counter = Counter(s)
        # set a flag initially to false that will tell us if we need to add an odd letter
        # into the middle of the palindrome at the end
        is_odd = False
        
        # loop through a list of only the values 
        for i in counter.values():
            # if there is only one occurance of a letter in the string set the flag to true
            if i == 1:
                count_odd = True
            # if there is an even number of occurances add all of them to the palindrome
            elif i % 2 == 0:
                max_length += i
            # if there is an odd number of occurances that isnt 1 add all but one to the palindrome
            else:
                max_length += i - 1
                # if flag already not set to true set the flag
                count_odd = True

        # if no odd letter orrurances in s return the max length
        if not count_odd:
            return max_length
        # if there are odd occurances return max legnth plus 1 ( essentially add an odd letter to the middle of the palindrome )
        else:
            return max_length + 1