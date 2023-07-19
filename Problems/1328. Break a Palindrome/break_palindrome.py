class Solution:
    def breakPalindrome(self, palindrome):
        for i in range(len(palindrome) // 2): # loop though only half of the string because the second half will be the same as the first half
            if palindrome[i] != "a": # if the letter at the current index is not "a" replace that letter with "a"
                return palindrome[:i] + "a" + palindrome[i + 1:] # [:i] = all of the letters before the current i index and [i + 1:] is all of the index after index i
            
        if len(palindrome) > 1: # if the solution is not found in the initial for loop and the len(palindrome) is greater than 1 you can return [:-1] = all indexes before last index and add "b"
            return palindrome[:-1] + "b" # an example of this could be "aba" the intial for loop will only loop though one index becuase 3//2 = 1 and you cannot replace the "b" with an a so you need to replace the last letter wth a "b"
        else:
            return "" # if the palindrome variable is less than one letter long then it cannot become not a palindrome so return an empty string