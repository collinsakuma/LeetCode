class Solution:
    def chalkReplacer(self, chalk, k):

        k %= sum(chalk) # take the remainder of the first pass of questions to get the remaining pieces of chalk left after all students have answered one question
                        # reduces the amount of times all students need to be iterated over by 1

        for i in range(len(chalk)): # iterate though all students by index
            if chalk[i] > k: # if the chalk needed by student is greater than the current number of chalks (k) then that student will need to replace the chalks
                return i # return the index of the student that needs to replace the chalks
            k -= chalk[i] # reduce the amount of chalks (k) by the amount needed by that student