class Solution:
    def isPrefixString(self, s, words):
        for i in range(1, len(words) + 1):
            # loop through a range of 1 to len of words array plus one ( plus 1 to account for 0 index)
            if s == ''.join(words[:i]):
                # - concatenate a new string with each element in the words array
                # - after word at index i is added to the string check if it is equal to s
                # - words are concatenated until all elements have been added to string 
                # - if at the end of the loop it does not equal s return false as a prefix cannot be created
                return True
        return False
