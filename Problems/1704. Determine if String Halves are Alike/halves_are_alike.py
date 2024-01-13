class Solution:
    def halvesAreAlike(self, s):
        half = len(s) // 2 # get the value of half the string
        a, b = s[:half], s[half:] # set two  variables a and b to the two halves of the string
        vowels = "aeiouAEIOU" # set a string with all possible vowels, lower and upper case

        vowels_a, vowels_b = 0, 0 # set two variables to keep track of count of vowels in each half of the string

        for i in range(len(a)): # loop through range of half the string length
            # check each letter in the string if its a vowel, if a vowel incrase the count for that half string
            if a[i] in vowels:
                vowels_a += 1
            if b[i] in vowels:
                vowels_b += 1

        return vowels_a == vowels_b # if both halves have an equal count of vowels return True, else return False