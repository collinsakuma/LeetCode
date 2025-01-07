class Solution:
    def stringMatching(self, words):
        output = [] # words that are substrings in other words

        # loop through words to check if they are substrings
        for substring in words:
            # loop through words a second time
            for word in words:
                # if the substring is the word skip 
                if substring == word:
                    None
                # if the word is a substring of another word and not already in the output list add it
                elif substring in word and substring not in output:
                    output.append(substring)
        
        return output # return list of substrings