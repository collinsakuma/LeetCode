class Solution:
    def reverseString(self, s):
        s.reverse()

    def reverseStringTwo(self, s):
        # - can not use s = s[::-1]
        # - must use s[:] becuase s[:] points to the actual elements in the list and modifies each one
        s[:] = s[::-1]

    def reverseStringThree(self, s):
        front, back = 0, len(s) - 1

        while front < len(s) // 2:
            s[front], s[back] = s[back], s[front]
            front += 1
            back += 1

            