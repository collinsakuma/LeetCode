class Solution:
    def groupAnagrams(self, strs):
        output = {} # dict to keep track of the letters in the word as the key, and the words that all contain those letters as the values

        for word in strs: # loop though the strings in strs
            sorted_word = ''.join(sorted(word)) # sort the letters into a string

            if sorted_word not in output: # if the sorted letters is not already in the dict
                output[sorted_word] = [word] # add the sorted string as the key with a list as its value containing the word
            else: # if the sorted string of word is in the dict
                output[sorted_word].append(word) # append the word to its matching list

        return list(output.values()) # return the dict as a list only caintaing the values from the dict