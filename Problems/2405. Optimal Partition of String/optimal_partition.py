class Solution:
    def partitionString(self, s):
        count = 0 # keep track of substring partitions of s
        substring = "" # hold value of current substring of unique elements being built
        
        for i in s: # loop though letters in s
            # check if letter is already in substring, substrings must be build of unique letters
            if i in substring:
                # if i in substring, increase count of partitions by 1 and reset the substring to only contain i
                count += 1
                substring = i
            else: # if i is not in substring add i to substring
                substring += i

        return count + 1 # add 1 to count because there is a substring that is not counted for after loop ends