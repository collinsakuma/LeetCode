class Solution:
    def maximum69Number(self, num):
        str_num = list(str(num)) # convert the number into a list 

        for i, j in enumerate(str_num): # use enumerate to loop though the list of numbers while keeping track of the index value
            if j == "6": # at the first instance of a 6 replace it with a 9
                str_num[i] = "9"
                break # only one change operation can be made so break from the loop if a 6 is changed 
        return int("".join(str_num)) # convert the list back into a number and return it