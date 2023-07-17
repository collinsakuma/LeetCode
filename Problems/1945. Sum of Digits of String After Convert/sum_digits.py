class Solution:
    def getLucky(self, s, k):
        new_s = "" # variable to convert the letters into a string with the number values
        for letter in s: # itterate thought the string
            new_s += str(ord(letter) - 96) # conver each letter to its number complement and add it to the new_s string
        while k != 0: # k denotes the times the operation needs to be performed so continue the loop while k does not equal 0
            transform = 0 # transform value to sum numbers in string
            for num in str(new_s): # loop trough the new_s 
                transform += int(num) # add each digit in new_s to the transform variable as an integer
            new_s = transform # set transform as the new value of new_s
            k -= 1 # reduce the number of times k needs to be iterated by 1 as one iteration has been completed. 
        return new_s # if while loop is exited return the value of new_s