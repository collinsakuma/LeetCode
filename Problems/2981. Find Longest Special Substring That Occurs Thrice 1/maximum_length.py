class Solution:
    def maximumLength(self, s):
        n = len(s)
        # create a dict to hold substrings and the count of how many times they occur
        sub_strings = dict()

        # loop through range of n
        for start in range(n):
            # loop through range from start to end
            for end in range(start, n):
                # check if next letter is the same character
                # if not add the substring to the dictionary
                if s[start] != s[end]: break
                # check if the substring is in the dict, if not create a new entry else increment the sibstrings count
                if s[start:end + 1] not in sub_strings:
                    sub_strings[s[start:end + 1]] = 1
                else:
                    sub_strings[s[start:end + 1]] += 1
        
        # create a list of substring that occur only three or more times
        sub_strings = [string for string, count in sub_strings.items() if count >= 3]

        # if there are no substrings that occur at least three times return -1
        if not sub_strings:
            return -1
        # else return the length of the longest substring
        else:
            return len(max(sub_strings, key=len, default=None))