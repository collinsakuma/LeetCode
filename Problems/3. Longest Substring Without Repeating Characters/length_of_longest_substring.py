class Solution:
    def lengthOfLongestSubstring(self, s):
        # edge case, if string is empty then return 0
        if not s:
            return 0
        
        # set two pointers
        left, right = 0, 1
        # set the initial substring to first character in s
        sub_string = s[0]
        # variable to hold the max length of a substring that meets requirements
        max_length = 0

        # while window is still in range of the string
        while left < len(s) and right < len(s):
            # is letter isnt already in the substring add it to the substring
            if s[right] not in sub_string:
                sub_string += s[right]
                # slide window right
                right += 1
            # if s[right] is already in the substring
            else:
                # check for a new max length
                max_length = max(max_length, len(sub_string))
                # increment the left side of the window
                left += 1
                # set a new right side of the window
                right = left + 1
        # return the length of the longest substring build of unique characters
        return max(max_length, len(sub_string))