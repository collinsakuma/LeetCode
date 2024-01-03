class Solution:
    def findMatrix(self, nums):
        output = [[]] # initalize empty matrix

        for num in nums: # loop though numbers in nums
            flag = True # set flag if flag is True after each num is looped then a new row must be created
            for i in range(len(output)): # loop though range of current rows in the matrix
                # check each row if num is already in the rows of the matrix
                if num not in output[i]:
                    output[i].append(num) # add num into the first row that num isnt it
                    flag = False # set flag to False ( num has been aded to a row )
                    break # num has been added to a row stop looping through rows and move to next number

                if flag: # if num has not been added to an existing row ( i.e. it already exist in all current rows ) create a new row
                    output.append([num]) # create new row with num as its only element
        
        return output