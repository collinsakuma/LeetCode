class Solution:
    def reverseString(self, s):
        s.reverse()

    def reverseStringTwo(self, s):
        # - can not use s = s[::-1]
        # - must use s[:] becuase s[:] points to the actual elements in the list and modifies each one
        s[:] = s[::-1]