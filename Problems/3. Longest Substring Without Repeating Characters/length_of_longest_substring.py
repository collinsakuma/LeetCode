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
    
    def lengthOfLongestSubstring(self, s):
        # max length of a substring with no repeating characters
        max_length = 0
        # set of unique characters
        char_set = set()
        # left pointer 
        left = 0

        for right in range(len(s)):
            # if character not in character set
            if s[right] not in char_set:
                # add character to the set of unique characters
                char_set.add(s[right])
                # check if a new max length is found
                max_length = max(max_length, right - left + 1)
            # if character is already in the character set
            else:
                # while the characters is in the set
                while s[right] in char_set:
                    # remove character at pointer left from the set 
                    # keep removing left most character untill character at index right is not longer in the set
                    char_set.remove(s[left])
                    # increment left 
                    left += 1
                # once removed left character that is the same as right, add right to the set
                char_set.add(s[right])
        return max_length