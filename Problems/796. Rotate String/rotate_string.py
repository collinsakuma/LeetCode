class Solution:
    def rotateString(self, s, goal):
        # if the goal string is longer than s then goal cannot be in s
        if len(goal) < len(s):
            return False
        
        s = s + s # create a circular string

        # loop through s
        for i in range(len(s)):
            # if goal in s return True
            if s[i:i + len(goal)] == goal:
                return True
        
        return False # if goal not found return False