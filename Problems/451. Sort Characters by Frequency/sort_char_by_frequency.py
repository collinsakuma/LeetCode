class Solution:
    def frequencySort(self, s):
        # set to empty dicts to keep track of upper and lower case letters respectively
        u_dict = {}
        l_dict = {}

        for i in s: # loop through letters in s
            if i.isupper(): # if letters is upper case
                # if not in u_dict add a new item, else increment dict entry with key i
                if i not in u_dict: u_dict[i] = i
                else: u_dict[i] += i
            else: # do the same if the letter is lower case
                if i not in l_dict: l_dict[i] = i
                else: l_dict[i] += i
        
        list_letters = u_dict | l_dict # combine the two dictionaries 

        # sort the list of dict values using a key of length and in reverse order, join all as a string
        return ''.join(sorted(list_letters.values(), key=len, reverse=True))