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
    


    # second solution, two pointer, faster runtime but higher memory usage( only .1 mb )
    
    def reverseVowelsTwo(self, s: str) -> str:
        vowels = "aAeEiIoOuU" # string of vowels capital and lowercase
        list_s = list(s) # conver string s into a list

        # set two pointer variables to opposite ends of the list
        left = 0
        right = len(s) - 1
            
        while left < right: # loop untill the two pointers intersect
            if list_s[left] in vowels and list_s[right] in vowels: # if both left and right are vowels switch the two values for eachother
                list_s[left], list_s[right] = list_s[right], list_s[left]
                # increment both left and right in the appropriate direction
                left += 1
                right -= 1
            
        # if left and right are both not vowels check each individually    
            elif list_s[left] not in vowels: # check if left if not a vowel
                left += 1 # if not increment left by 1
            
            elif list_s[right] not in vowels: # check if right is not a vowel
                right -= 1 # if not increment(subtract) right by 1
        
        return "".join(list_s) # rejoin the list into a string and return it