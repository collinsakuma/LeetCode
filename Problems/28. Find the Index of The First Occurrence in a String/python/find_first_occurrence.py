class Solution:
    def strStr(self, haystack, needle):
        if needle not in haystack:
            # if the needle is not in the haystack return -1
            return -1
        else:
            return haystack.find(needle)
            # return the index where the needle starts in the haystack. 