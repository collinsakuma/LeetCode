class Solution:
    def customSortString(self, order, s):
        # sorted_s will be the final sorted s using the order given in order
        # set_order and set_s will be th characters already traversed in order and s
        sorted_s = set_order = set_s = ''

        # loop though order
        for char in order:
            # if char is in s and the char has not been seen already
            if char in s and char not in set_order:
                # add char to the string sorted_s, add it as many times as its frequency in s
                sorted_s += char * s.count(char)
                set_order += char # add that character to the seen letters in set_order
        
        # loop though string s
        for i in s:
            # if i isnt in the sort order string given and i has not been seen in current loop
            if i not in order and i not in set_s:
                # add i to the string sorted_s, add it as many times as its frequency in s
                sorted_s += i * s.count(i)
                set_s += i # add i to the seen letters in set_s

        return sorted_s # return the sorted string