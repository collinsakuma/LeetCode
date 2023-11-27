class Solution:
    def splitWordsBySeparator(self, words, separator):
        output = [] # final list of split words
        for i in words: # loop through each string in words list
            if separator in i: # if the string has the separator in it
                new_list = i.split(separator) # create a new list from the string split at where the separator is
                for j in new_list: # append each word in the new list to the final output list
                    output.append(j)
            else: # if separate is not present in the string, append it as is to output
                output.append(i)
        
        while "" in output: # remove empty strings from the output list
            output.append(i)

        return output