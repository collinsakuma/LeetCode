class Solution:
    def contConsistentStrings(self, allowed, words):
        count = 0 # count of consistent words

        # loop through words
        for word in words:
            # set flag to true
            flag = True

            # loop through a set of characters in word
            for ch in set(word):
                # if the character not in the allowed string
                if ch not in allowed:
                    # set flag to false
                    flag = False
                    # break out of the loop
                    break
                # if flag is false break out the loop
                if not flag: break
            # if flag is true then word is consistent increment count
            if flag: count += 1
        
        return count