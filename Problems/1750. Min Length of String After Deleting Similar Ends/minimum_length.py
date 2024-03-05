class Solution:
    def minimumLength(self, s):
        # set two pointers
        left, right = 0, len(s) - 1

        # start a loop and countiue traversal if:
        # - two pointers have not intersected
        # - the two pointers index values are the same
        while left < right and s[left] == s[right]:
            # set a character value to s[left] 
            char = s[left]
            
            # find the left prefix
            # while left pointer has not intersected right and all indexes equal char
            while left <= right and s[left] == char:
                left += 1 # increment left side pointer
            
            # find a matching right side suffix
                # while right pointer is greater than left and character is still equal to right pointer value
            while right >= left and s[right] == char:
                right -= 1 # increment right side pointer down

        return right - left + 1 # what remains of s is set between right and left, return the # of remaining characters
