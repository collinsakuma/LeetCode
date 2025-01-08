class Solution:
    def countPrefixSuffixPairs(self, words):
        index_pairs = 0 # number of pairs of words where i is prefix and suffix of j

        # check if prefix and suffix funciton
        def isPrefixAndSuffix(str1, str2):
            # if string being checked as prefix is longer than word return False
            if len(str1) > len(str2): return False

            # check if str1 is prefix and suffix of str2
            return str1 == str2[:len(str1)] and str1 == str2[-len(str1):]
        
        # loop through range of words twice only indexes where i < j
        for i in range(len(words)):
            for j in range(i, len(words)):
                # check if prefix and suffix
                if isPrefixAndSuffix(words[i], words[j]):
                    # if true increment number of pairs found
                    index_pairs += 1

        return index_pairs