class Solution:
    def decodeString(self, s):
        stack = []
        curNum = 0
        curString = ''

        for c in s:
            # if c is an opening bracket
            # add to the stack list first the curString, and then the curNum
            # reset the curString and curNum variables as well
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            # if c is a closing bracket
            # first .pop() the curNum variavble from stack that represents how many times the str must be repeated
            # second .pop() the str from the stack that represents the previous string added
            # set the current string variable to prevString plus num * curString
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            # if c is a number, save that number in the curNum variable
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            # if c is a letter just add it to the curString variable
            else:
                curString += c
        return curString