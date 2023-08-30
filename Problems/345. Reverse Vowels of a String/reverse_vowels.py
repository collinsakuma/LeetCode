class Solution:
    def reverseVowels(self, s):
        vowels = "aAeEiIoOuU" # string of all vowels capital and lowercase
        vowels_in_s = [] # empty list to append vowels found to
        output = "" # output string
 
        for letter in s: # loop though letters in s
            if letter in vowels: # if a letter is a vowel append it to vowels_in_s list
                vowels_in_s.append(letter)

        for i in range(len(s)): # second loop for range of lenght s
            if s[i] in vowels: # if the letter at the index is a vowel add the letter at the end of vowels_in_s list
                output += vowels_in_s.pop(-1)
            else: # if letter at index is not a vowel add the letter from s at the index to the output
                output += s[i]
        
        return output # return the new string with the vowels reversed