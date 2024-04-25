from collections import Counter

class Solution:
    def canConstruct(self, s, k):
        # if there are more palindromes to be created than letters available
        # there is no way for k palindromes to be created
        if len(s) < k:
            return False
        
        # create a count dict using Counter
        count = Counter(s)
        num_odd = 0

        # loop through a list of how many times each letters apeears in s
        for num in count.values():
            # count the number of letters whos occur an odd number of times in s
            if num % 2 != 0:
                num_odd += 1
        
        # if the count of letters that appear an odd number of times in s is greater than k
        # then k number of valid palindromes cannot be created because odd count letters must
        # be distributed between the different palindromes
        if num_odd > k:
            return False
        
        return True