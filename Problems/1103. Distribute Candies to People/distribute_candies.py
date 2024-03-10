class Solution:
    def distributeCandies(self, candies, num_people):

        list_people = [0] * num_people # create a list of 0's with a length equal to the num_people
        index = 1 # create an index variable to keep track of how many rounds of candies have been given out

        while candies > 0: # create a loop that will continue to run while there are still candies left to give out
            if candies > index: 
                list_people[(index - 1) % num_people] += index
            else:
                list_people[(index - 1)  % num_people] += candies

            candies -= index
            index += 1
        return(list_people)